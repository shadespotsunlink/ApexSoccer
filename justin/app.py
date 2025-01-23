from flask import Flask, request, jsonify, render_template
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

# Configure your email settings
EMAIL_ADDRESS = "your-email@example.com"
EMAIL_PASSWORD = "your-email-password"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

@app.route('/')
def index():
    return render_template('index.html', academy_name="APEX FOOTY ACADEMY")

@app.route('/services')
def services():
    return render_template('services.html', academy_name="APEX FOOTY ACADEMY")

@app.route('/about')
def about():
    return render_template('about.html', academy_name="APEX FOOTY ACADEMY")

@app.route('/api/book', methods=['POST'])
def book_session():
    try:
        data = request.json
        
        # Create email message
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = EMAIL_ADDRESS
        msg['Subject'] = f"New Booking Request from {data['name']}"
        
        body = f"""
        New booking request:
        
        Name: {data['name']}
        Email: {data['email']}
        Phone: {data['phone']}
        Service: {data['service']}
        Experience Level: {data['experience']}
        Message: {data['message']}
        Newsletter: {'Yes' if 'newsletter' in data else 'No'}
        """
        
        msg.attach(MIMEText(body, 'plain'))
        
        # Send email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
        
        return jsonify({"message": "Booking received successfully"}), 200
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": "An error occurred processing your booking"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080) 