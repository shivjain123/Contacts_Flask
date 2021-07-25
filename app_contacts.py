from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def HelloWorld():
    return "Hello World"

contacts = [{'id': 1,
          'name': "Shiv",
          'contact': 9301664087,
    },
    {
        'id': 2,
        'name': "Swapnil",
        'contact': 8120690868,
}]

@app.route('/get_data_contacts')
def Get_Task():
    return jsonify({
        'data': contacts
    })

@app.route('/add_data_contacts', methods=["POST"])
def Add_Task():
    if (not request.json):
        return jsonify({
            'status': "Error",
            'message': "Please Provide the Data."
        })
    else:
        contact = {
            'id': contacts[-1]['id'] + 1,
            'name': request.json["name"],
            'contact': request.json.get("contact", ''),
        }
        contacts.append(contact)
        return jsonify({
            'status': "Success!",
            'message': "Your Contact Details were successfully added."
        })


if __name__ == '__main__':
    app.run()