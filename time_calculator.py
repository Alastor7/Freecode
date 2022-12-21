# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 18:23:56 2022

@author: cayoj
"""
 

day1 = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
hour1 = [00, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
minute1 = 0

hour2 = [00, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
minute2 = 0

p_a = ["AM", "PM"]


start = 0

while True:
    print("""
    Do you want star the time calculator?
    
    1) Yes
    2) No
    
    
    """)
    start = int(input("Choose an obtion: ") )     
    
    if start == 1:
        
       day1 = day1[int(input("Put the day with numbers between 0 to 6: "))]
       hour1 = hour1[int(input("Put the hour with numbers between 0 to 12: "))]
       minute1 = int(input("Put the minute: "))
       p_a = p_a[int(input("Put the AM(0) or PM(0) with numbers between 0 to 1: "))]
       
       print("This is the hour that you put at first", day1, hour1, ":", minute1, p_a)
       t = [day1, hour1, minute1, p_a]
       
       print("  ")
       hour2 = hour2[int(input("Put the hour with numbers between 0 to 12 for the second: "))]
       minute2 = int(input("Put the minute: "))
       
       print("This is the hour that you put at second", hour2, ":", minute2)
       t2 = [hour2, minute2]
       
       x = 0 
       g = 0
       timepass = 0
       
       
           
       if t[2] >= 60:
               
               t[2] = t[2] - 60
               t[1] = t[1] + 1
               
       
           
       
       
                   
                  
            
       if 0 <= t[1] <= 11 and 0 <= t[2] <= 59:
                
                t[3] = "AM"
                
                 
            
       elif 12 <= t[1] <= 23 and 0 <= t[2] <= 59:
                
                t[3] = "PM"

            
       if t[3] == "PM":
                
                x = t[1] + t2[0]
                g = t[2] + t2[1]
                
                if g > 60:
                    
                    x = x + 1
                    g = g - 60
                    
                
                if x > 24:
                    
                    x = x - 24
                    
            
       elif t[3] == "AM":
                
                x = t[1] + t2[0]
                g = t[2] + t2[1]
                
                if g > 60:
                    
                    x = x + 1
                    g = g - 60
             
                while x > 24: 
                    
                    timepass = 0
                    timepass = timepass + 1
                    
                    if x > 24:
                    
                        x = x - 24
                    
                    if x >= 12:
                        
                        x = 12 + x
                        
                        
        
             
       if 00 <= x <= 11 and 00 <= g <= 59:
                 
                 t[3] = "AM"
                 x = x - 12
                 
             
       elif 12 <= x <= 23 and 00 <= g <= 59:
                 
                 t[3] = "PM"
                 
                 
             
       add_time = (x, g, t[3])
       
       if timepass > 1:
           print(add_time, timepass, "days later")
           
       else:
           print(add_time)     
                      
           
    else:
        print("The programme ended")
        break
