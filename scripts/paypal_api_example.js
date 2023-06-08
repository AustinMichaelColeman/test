const fetch = require('node-fetch');

const PAYPAL_API_URL = 'https://api.paypal.com';

const getPayPalData = async (accessToken) => {
  const response = await fetch(`${PAYPAL_API_URL}/v1/payments/payment`, {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${accessToken}`
    }
  });

  if (!response.ok) {
    throw new Error(`HTTP error! status: ${response.status}`);
  }

  const data = await response.json();
  return data;
}

const accessToken = 'your-access-token-here';
getPayPalData(accessToken)
  .then(data => console.log(data))
  .catch(error => console.error(error));