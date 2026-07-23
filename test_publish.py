from server import publish_account_handoff

result = publish_account_handoff(
    html="""
<html>
  <body>
    <h1>Hello Pathlock</h1>
  </body>
</html>
""",
    metadata={
        "account_name": "Test Account",
        "account_id": "001PZ00000RxPpZYAV",
        "opportunity_id": "006TEST",
        "generated_by": "Account Handoff Agent",
    }
)

print(result)