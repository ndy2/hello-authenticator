import streamlit_authenticator as stauth

hashed_passwords = stauth.Hasher(['ndy', 'haha']).generate()
hello_authenticate = stauth.Authenticate(
    {
        "usernames": {
            "ndy": {
                "email": "jsmith@gmail.com",
                "name": "남득윤",
                "password": hashed_passwords[0]
            },
            "haha": {
                "email": "rbriggs@gmail.com",
                "name": "하하",
                "password": hashed_passwords[1]
            }
        }
    },
    "some_cookie_name",
    "some_signature_key",
    30,
    None,
    None
)