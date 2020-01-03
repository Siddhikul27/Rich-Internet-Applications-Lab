const Nexmo = require('nexmo');

const nexmo = new Nexmo({
  apiKey: 'yourApiKey',
  apiSecret: 'yourApiSecret'
});

/**
 * @param senderName : string => name to message sender that would appear on a receiver's phone
 * @param message : string => message to be sent to the numbers
 * @param phoneNumbers: an array of numbers to receive the message
 */
const sendBulkSms = (senderName, message, phoneNumbers) => {

  //Loop through each number and send sms message to
  for (let i = 0; i < phoneNumbers.length; i++) {
    let number = phoneNumbers[i];

    // ensure number starts with country code (in this case, Nigeria (234))
    number = number.startsWith('0') ? number.replace('0', '234') : number;
    
    nexmo.message.sendSms(senderName, number, message, (err, result) => {
      if (err) console.log(err);
      console.log(result);

      // after the message has been successfully sent to the last number, send a server response
      if(i === phoneNumbers.length - 1){
        console.log('message sent');
        // You can now return server response.
      }
    });
  }
};

sendBulkSms('HashCode', 'Hello World!', [0]);