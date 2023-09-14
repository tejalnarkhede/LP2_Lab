import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"hi|hello|hey",
     ["Hello!", "Hi there!"],
    ],
    [
        r"i want to book (.*)",
      ["Sure, please visit our website FUN TRAVEL Airline Agency into book a %1."],
    ],
    [
        r"what are the top destinations to visit",
     ["We have a list of top destinations on our website FUN TRAVEL Airline Agency, you can check it out there."],
    ],
    [
        r"what is the best time to visit (.*)",
     ["You can visit our website whenever you want. it is available 24/7."],
    ],
    [
        r"what is the fare for (.*) to (.*)",
     ["The fare for %1 to %2 is Rs. 10000. For more detailed information visit FUN_TRAVEL.com"]
    ],
    [
        r"what is the cheapest fare to (.*)",
     ["The cheapest fare to %1 is Rs5000. For more detailed information visit FUN_TRAVEL.com"],
    ],
    [
        r"Okay|Ok|K",
     ["Yeah"],
    ],
    [
        r"What kind of travel packages do you offer?",
     ["We offer a wide range of travel packages including all-inclusive vacations, adventure tours, cruise packages, honeymoon packages, and more."]
    ],
    [
        r"Can you help me plan a custom trip to a specific destination?",
        ["Absolutely! We specialize in creating customized travel itineraries based on your preferences and budget. Just let us know your destination, dates, and travel preferences, and we'll take care of the rest."]
    ],
    [
        r"What kind of travel insurance options do you provide?",
        ["We offer comprehensive travel insurance plans that cover everything from trip cancellation and medical emergencies to lost baggage and flight delays. Our team can help you select the right insurance plan based on your travel needs."]
    ],
    [
        r"Can you help me book flights and hotels for my trip?",
        ["Yes, we can help you book flights, hotels, rental cars, and any other travel-related services that you need. Our team has access to a wide range of travel suppliers and can help you find the best deals."]
    ],
    [
        r"How do I make a reservation for a travel package?",
        [" You can make a reservation for a travel package by contacting our travel agency either through our website or by phone. Our team will be happy to assist you with the booking process and answer any questions you may have."]
    ],
    [
        r"What kind of payment options do you accept?",
        ["We accept various payment options including credit cards, bank transfers, and online payment methods. Our team will provide you with detailed information on payment options when you make a reservation."]
    ],
    [
        r"What if I need to cancel my reservation?",
        ["We understand that travel plans can change, and we have flexible cancellation policies in place for most of our travel packages. Please check the terms and conditions of your specific package, or contact our team for more information on cancellation policies."]
    ],
    [
        r"Do you offer any special discounts or promotions?",
        ["Yes, we regularly offer special discounts and promotions on our travel packages. Check our website or contact our team to find out about any current offers."]
    ]
]

chatbot = Chat(pairs, reflections)

print("Welcome to FUN TRAVEL Air Line Agency")

chatbot.converse()