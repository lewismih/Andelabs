""" I define a function data_type that receives an entry.
 It then should check for the appropriate type and respond accordingly"""

def data_type (entry):
  
  if type (entry) == None:
    return entry
  
  #check for a string and return its length
  if type (entry) == str:
    return len (entry)
   
  #check for bool value and returns the boolean
  elif type (entry) == bool:
    return entry
   
  #check for integer value and responds in relation to 100
  elif type (entry) == int:
      if entry < 100:
          return "less than 100"
      
      elif entry > 100:
          return "more than 100"
      
      else:
          return "equal to 100"
   
  #check for a list 
  elif type (entry) == list:
    try:
      if entry[2]:
          return entry[2]
    except (IndexError):
          return None
      
  #check for empty entry and return no value
  else:
    return "no value"