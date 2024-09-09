from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['POST'])
def save_message():
    name = request.form['name']
    message = request.form['message']
    with open('message.txt', 'a') as file:
        file.write(f'Name: {name}\nMessage: {message}\n\n')
    return render_template_string('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Thank You</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f0f8ff;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                }
                .container {
                    background-color: #fff;
                    padding: 20px;
                    border-radius: 10px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                }
                h1 {
                    color: #ff69b4;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Thank you for your message, {{ name }}!</h1>
            </div>
        </body>
        </html>
    ''', name=name)

if __name__ == '__main__':
    app.run(debug=True)
