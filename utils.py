import requests


def get_case_by_id(case_id, token):
    """
    Fetches case details by ID from the Duval Clerk service.

    :param case_id: The ID of the case to retrieve.
    :param token: The authentication token.
    :return: The response as a dictionary if successful, or an error message.
    """
    url = "https://core.duvalclerk.com/internal/CoreWebSvc.asmx/GetCaseById"

    # Payload
    payload = {"token": token, "returnTabId": 0, "caseID": case_id, "simCtrl": 0}

    # Headers
    headers = {
        "accept": "*/*",
        "content-type": "application/json; charset=UTF-8",
        "origin": "https://core.duvalclerk.com",
        "referer": "https://core.duvalclerk.com/CoreCms.aspx?mode=PublicAccess",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "x-requested-with": "XMLHttpRequest",
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}