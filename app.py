import requests
import json

def main():
    print("=== Bajaj Finserv Health Qualifier Integration Script ===")
    
    # Candidate details
    payload = {
        "name": "Rachit Dhakad",
        "regNo": "0827CS231205",
        "email": "rachitdhakad230998@acropolis.in"
    }
    
    print("\n[Step 1] Sending POST request to generate webhook URL...")
    init_url = "https://bfhldevapigw.healthrx.co.in/hiring/generateWebhook/PYTHON"
    
    try:
        response = requests.post(init_url, json=payload)
        response.raise_for_status()
        res_data = response.json()
    except Exception as e:
        print(f"Error generating webhook: {e}")
        return

    # Extract webhookUrl and accessToken
    webhook_url = res_data.get("webhookUrl") or res_data.get("webhook")
    access_token = res_data.get("accessToken")
    
    if not webhook_url or not access_token:
        print(f"Error: Response did not contain webhookUrl or accessToken. Response: {res_data}")
        return
        
    print("[Step 2] Webhook URL and Access Token successfully retrieved.")
    print(f"Webhook URL: {webhook_url}")
    print(f"Access Token: {access_token}")

    # Step 3: Print assignment link (Registration number ends in 5 - Odd)
    print("\n[Step 3] Because your regNo (0827CS231205) ends in an odd number (5), here is the assignment link:")
    print("https://drive.google.com/file/d/1q8F8g0EpyNzd5BWk-voe5CKbsxosk.JWY/view?usp=sharing")
    print("=" * 70)
    
    # Step 4: Wait for user to paste their SQL query
    try:
        print("\nPlease solve the SQL query from the assignment and paste it below.")
        final_query = input("Enter your final solved SQL query: ").strip()
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        return

    if not final_query:
        print("Error: SQL query cannot be empty.")
        return

    # Step 5: Send POST request to the dynamic webhookUrl
    print("\n[Step 4] Sending the SQL query to the dynamic webhook URL...")
    headers = {
        "Authorization": access_token,
        "Content-Type": "application/json"
    }
    submit_payload = {
        "finalQuery": final_query
    }
    
    try:
        res_submit = requests.post(webhook_url, headers=headers, json=submit_payload)
        print(f"Submission Status Code: {res_submit.status_code}")
        print("Response Content:")
        try:
            print(json.dumps(res_submit.json(), indent=2))
        except ValueError:
            print(res_submit.text)
    except Exception as e:
        print(f"Error sending final query to webhook: {e}")

if __name__ == "__main__":
    main()
