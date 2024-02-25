from nltk.chat.util import Chat, reflections

# Define the pairs for the chatbot
pairs = [
    [
        r"hi|hello|hey|good (morning|afternoon|evening)",
        [
            "Hello! I'm your engineering stream chatbot. How can I assist you today?",
        ],
    ],
    [
        r"(.*)\bengineering\b(.*)",
        [
            "Would you like to inquire about engineering branches or top universities?",
        ],
    ],
    [
        r"\b(branches)\b",
        [
            "Here are some common branches of engineering:\n1. Computer Science\n2. Electrical and Electronics\n3. Mechanical\n4. Civil\n5. Chemical\n6. Aeronautical and Aerospace\n7. Marine\n8. Biomedical\n\nWhich branch are you interested in?"
        ],
    ],
    [
        r"\b(computer|computers|computer science)\b(.*)",
        [
            "Computer Science engineering is a great choice! Would you like to know about the top universities for Computer Science engineering?",
        ],
    ],
    [
        r"\b(electrical|electronics)\b(.*)",
        [
            "Electrical and Electronics engineering offers exciting opportunities. Would you like to know about the top universities for Electrical and Electronics engineering?",
        ],
    ],
    [
        r"\b(mechanical)\b(.*)",
        [
            "Mechanical engineering deals with the design and manufacturing of mechanical systems. Would you like to know about the top universities for Mechanical engineering?",
        ],
    ],
    [
        r"\b(civil)\b(.*)",
        [
            "Civil engineering involves the design and construction of infrastructure. Would you like to know about the top universities for Civil engineering?",
        ],
    ],
    [
        r"\b(chemical)\b(.*)",
        [
            "Chemical engineering focuses on the design and operation of chemical plants. Would you like to know about the top universities for Chemical engineering?",
        ],
    ],
    [
        r"\b(aeronautical|aerospace)\b(.*)",
        [
            "Aeronautical and Aerospace engineering deals with aircraft and spacecraft design. Would you like to know about the top universities for Aeronautical and Aerospace engineering?",
        ],
    ],
    [
        r"\b(marine)\b(.*)",
        [
            "Marine engineering involves the design and maintenance of ships and other maritime equipment. Would you like to know about the top universities for Marine engineering?",
        ],
    ],
    [
        r"\b(biomedical|bio-medical)\b(.*)",
        [
            "Biomedical engineering applies engineering principles to biology and medicine. Would you like to know about the top universities for Biomedical engineering?",
        ],
    ],
    [
        r"\b(universities|top universities)\b",
        [
            "Here are the top 10 universities globally:\n1. Massachusetts Institute of Technology (MIT)\n2. Stanford University\n3. Harvard University\n4. California Institute of Technology (Caltech)\n5. University of Oxford\n6. ETH Zurich - Swiss Federal Institute of Technology\n7. University of Cambridge\n8. Imperial College London\n9. University of Chicago\n10. National University of Singapore (NUS)",
        ],
    ],
    [
        r"\b(quit|exit)\b",
        [
            "Thank you for chatting with me. If you have more questions, feel free to ask later!",
        ],
    ],
    [
        r"(.*)",
        [
            "I'm sorry, I'm not sure how to help with that. Could you please be more specific?",
        ],
    ],
]

print("Hello! Welcome to the engineering stream chatbot.")
print(
    "How can I assist you today? You can inquire about engineering branches, inquire about top universities, or type 'quit' to exit."
)

chat = Chat(pairs, reflections)
chat.converse()
