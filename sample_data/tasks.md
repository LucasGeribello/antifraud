3.1 - Understand the Industry

1.Explain the money flow and the information flow in the acquirer market and the role of the main players:
Money Flow
A customer pays using a credit/debit card.
The transaction is authorized by the issuer (the customer's bank).
Funds are settled from the issuer to the acquirer (the merchant’s bank).
The acquirer deposits the money (minus fees) to the merchant’s account.

Information Flow
The payment gateway captures transaction details.
This data goes to the acquirer, who routes it to the card network (Visa, MasterCard).
The card network checks with the issuer for authorization.
Response flows back: issuer → card network → acquirer → gateway → merchant.


2. Explain the difference between acquirer, sub-acquirer and payment gateway and how the flow explained in question 1 changes for these players.

Roles of the Main Players
Acquirer: The financial institution that processes credit/debit card payments on behalf of the merchant.
Sub-acquirer: Intermediaries that connect small merchants to the acquirer. They aggregate transactions and often provide additional services (e.g., Stone, PagSeguro).
Payment Gateway: A tech layer that captures, encrypts, and transmits payment data between the merchant and the acquirer (e.g., Stripe, Adyen).

Changes in the Flow
If a sub-acquirer is involved, the merchant doesn’t interact directly with the acquirer.
If a payment gateway is used, the information flow is handled entirely by the gateway API, simplifying merchant operations.


3. Explain what chargebacks are, how they differ from cancellations and what is their connection with fraud in the acquiring world.

Chargebacks
Initiated by the customer through their issuer.
Usually a result of fraud, unauthorized use, or disputes.
The amount is forcibly reversed.
Impacts the merchant’s credibility and may involve fees or penalties.

Cancellations
Initiated by the merchant before or after settlement.
Voluntary and typically customer service related.
Does not affect fraud rates.

Connection with Fraud
High chargeback rates can indicate fraudulent transactions, especially if the pattern is:
Multiple chargebacks from the same user/card.
Unusual device IDs.
High-value purchases in short timeframes.


3.2 - Get your hands dirty

1. Analyze the data provided and present your conclusions (consider that all transactions are made using a mobile device).

830 Transactions Are Missing device_id
All transactions were supposedly made on mobile devices.
This could indicate:
Data collection issues or manipulation.
Attempts to remain anonymous — a common trait in fraudulent behavior.

31 Different Cards Were Used by Multiple Users
The same card_number (partially masked) was linked to different user_ids.
This may suggest:
Card sharing across accounts.
Stolen cards being used by fraudsters with multiple fake accounts.

No Device IDs Were Shared Across Users
No device_id was linked to more than one user.
This looks good on the surface, but the 830 missing device_ids weaken this conclusion.
It's possible that fraudsters are intentionally rotating devices or spoofing identifiers.

195 High-Value Chargebacks (Over 1,000)
These are high-risk transactions.
Potential causes:
Fraudulent purchases using stolen cards.
Intentional "friendly fraud" (users requesting chargebacks after receiving products).

2. Additional Data That Could Help Detect Fraud

To improve fraud detection, you could collect and analyze:

Data Type ----------------------------------------------- Why It's Useful
				
Device Geolocation	------------------------------------- Compare with shipping address and IP location
IP Address	---------------------------------------------	Identify multiple accounts using the same IP
Chargeback History per User/Card	----------------------- Spot repeat offenders
Time Between Transactions	-------------------------------	High frequency in a short period can indicate bot activity or fraud
Sign-up vs. Transaction Time ----------------------------	Quick registration and purchase may indicate a scam
Merchant vs. Chargeback Rate	---------------------------	See if specific merchants are unusually risky