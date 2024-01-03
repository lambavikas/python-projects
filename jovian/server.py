import os, requests
from flask import Flask, render_template, jsonify

app = Flask(__name__)
port = int(os.environ.get('PORT', 3000))

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 10,00,000'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Delhi, India',
    'salary': 'Rs. 15,00,000'
  },
  {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote'
  },
  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'San Francisco, USA',
    'salary': '$150,000'
  }
]

@app.route("/")
def hello_jovian():
    return render_template('home.html', 
                           jobs=JOBS, 
                           company_name='Jovian')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

@app.route("/api/products")
def get_products():
    # Define the OData service endpoint for products
    odata_endpoint = "https://services.odata.org/Northwind/Northwind.svc/Products?$format=json"
    odata_endpoint = "https://iac-apps-dev-sample-srv.cfapps.us10.hana.ondemand.com/catalog/Books"

    # Make an HTTP GET request to retrieve product data
    response = requests.get(odata_endpoint)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        product_data = response.json()

        # Return the product data as JSON
        return jsonify(product_data)
    else:
        # Return an error message
        return jsonify({"error": f"Error: {response.status_code} - {response.text}"}), 500



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=port)