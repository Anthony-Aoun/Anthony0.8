import openai

openai.api_key  = "PUT_YOUR_PERSONAL_API_KEY"

def _listened(lst : list, input_text : str) -> bool:
    """
    Input: 
        - lst: [[a, b],[c],[d, e, f],...]
                  l1    l2     l3
        - input_text : user's input
    Output: 
        - bool
    Description: 
        if (a or b) and (c) and (d or e or f) in input text return True. If not return False
    """ 
    for sublst in lst:
        # check if at least one word from the mini-list is in the input sentence
        if any(word in input_text for word in sublst):
            # if found, continue to the next mini-list
            continue
        else:
            # if no word is found in the input sentence, return False
            return False
    # if we've checked all mini-lists and found at least one word in each return True
    return True



def echo(input_text):
    """
    repeats input
    """
    output_text = "You said, "+input_text
    return output_text

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",  # 'gpt-3.5-turbo', 'gpt-4'
        messages=[
            {"role": "system", "content": "You are a helpful assistant called Anthony0.8, and your owner's name is Anthony. Address your owner with respect using expressions like sir or chief or calling him by his name : Anthony."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.7,  # Controls the randomness of the output
        max_tokens=60    # Limits the length of the response
    )

    # Extract and return the content of the response
    return response['choices'][0]['message']['content']



def respond_to(input_text):
    """
    bot response to input_text
    """
    return chat_with_gpt(input_text)
