def correct_errors(text):
    # Replace '5' with 'S'
    text = text.replace('5', 'S')
    
    # Replace '0' with 'O'
    text = text.replace('0', 'O')
    
    # Replace '1' with 'I'
    text = text.replace('1', 'I')
    
    return text
