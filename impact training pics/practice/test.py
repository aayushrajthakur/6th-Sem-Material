import pywhatkit as pwk

# Using Exception Handling to avoid unexpected errors
try:
    # Sending message in WhatsApp in India using Indian dial code (+91)
    pwk.sendwhatmsg("+919909638694", "Hi, how are you?", 9, 5)
    print("Message Sent!") # Prints success message in console
except:
    print("Error in sending the message")