# # -*- coding: utf-8 -*-
# """
# Created on Sun Aug 22 05:02:41 2021

# @author: monir
# """

# import websockets
# import asyncio
# import json

# # -*- coding: utf-8 -*-1111
# """
# Created on Mon Jun 14 21:34:01 2021

# @author: monir
# """
# from bitmex_websocket import BitMEXWebsocket
# import logging
# import time
# import statistics
# import hashlib
# import hmac
# import requests
# import urllib.parse
# import json
# import asyncio
# import numpy as np
# import csv



# # Generates an API signature.
# # A signature is HMAC_SHA256(secret, verb + path + expires + data), hex encoded.
# # Verb must be uppercased, url is relative, expires must be unix timestamp (in seconds)
# # and the data, if present, must be JSON without whitespace between keys.
# def generate_signature(secret, verb, url, expires, data):
#     """Generate a request signature compatible with BitMEX."""
#     # Parse the url so we can remove the base and extract just the path.
#     parsedURL = urllib.parse.urlparse(url)
#     path = parsedURL.path
#     if parsedURL.query:
#         path = path + '?' + parsedURL.query

#     if isinstance(data, (bytes, bytearray)):
#         data = data.decode('utf8')

#     message = verb + path + str(expires) + data
#     signature = hmac.new(bytes(secret, 'utf8'), bytes(message, 'utf8'), digestmod=hashlib.sha256).hexdigest()
#     return signature


# def setup_logger():
#     # Prints logger info to terminal
#     global logger 
#     logger = logging.getLogger()
#     logger.setLevel(logging.INFO)  # Change this to DEBUG if you want a lot more info
#     ch = logging.StreamHandler()
#     # create formatter
#     formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
#     # add formatter to ch
#     ch.setFormatter(formatter)
#     logger.addHandler(ch)
#     return logger




#     #await asyncio.sleep(5)
#     #await asyncio.create_task(get_status())     


# async def capture_data(websocket,uri):
#         x=0
#         while x==0:
#             try:
#                 data = await websocket.recv()
#                 data = json.loads(data)
                
#                 try :
#                     x=data['data'][0]["lastPrice"]
#                     return(x)
#                 except KeyError:
#                     continue
#             except:
#                 print("Quitting")
#                 return 0            
    
                
                
            
#             #print(data)
               
        
#             #input("Press any key")
# async def main():
    
#     switchh=0
#     uri = "wss://www.bitmex.com/realtime?subscribe=instrument:XBTUSD"
#     while switchh==0:
#         try:
#             websocket=await websockets.connect(uri)
#             switchh=1
#             print("\nConnected")
#         except:
#             print("\nCould not Connect. Retrying in 5 seconds")
#             await asyncio.sleep(5)
#             continue
        
                            
     
#     while 1:
            
            
#             f = open("seconddata.json", "a+")
#             r = await asyncio.create_task(capture_data(websocket,uri))
#             while r==0:
#                 #while switchh==0:
#                     try:
#                         websocket=await websockets.connect(uri)
#                         print("Connected")
#                         break
#                     except:
#                         await asyncio.sleep(5)
#                         continue
    
#             if r!=0:
#                 print(r,end='\n')
#                 f.write(str(r)+'\n')
#                 f.close()
#             #await asyncio.sleep(0.1)

# asyncio.run(main())

# import websockets
# import asyncio
# import json
# import time
# from datetime import datetime, timedelta

# # ... (rest of your code remains unchanged) ...

# async def capture_data(websocket, uri):
#     while True:
#         try:
#             data = await websocket.recv()
#             data = json.loads(data)
            
#             try:
#                 last_price = data['data'][0]["lastPrice"]
#                 return last_price
#             except KeyError:
#                 continue
#         except:
#             print("Quitting")
#             return 0

# async def main():
#     captured_data = []  # Create an empty list to hold the captured data
#     last_capture_time = datetime.now()

#     switchh = 0
#     uri = "wss://www.bitmex.com/realtime?subscribe=instrument:XBTUSD"
#     while switchh == 0:
#         try:
#             websocket = await websockets.connect(uri)
#             switchh = 1
#             print("\nConnected")
#         except:
#             print("\nCould not Connect. Retrying in 5 seconds")
#             await asyncio.sleep(5)
#             continue

#     while True:
#         r = await asyncio.create_task(capture_data(websocket, uri))
#         if r == 0:
#             try:
#                 websocket = await websockets.connect(uri)
#                 print("Connected")
#             except:
#                 print("Reconnection failed. Retrying in 5 seconds")
#             await asyncio.sleep(5)
#             continue
    
#         print(r, end='\n')

#         # Check if a minute has passed since the last capture
#         current_time = datetime.now()
#         if current_time - last_capture_time >= timedelta(minutes=1):
#             captured_data.append({"timestamp": current_time.timestamp(), "last_price": r})
#             last_capture_time = current_time
            
#             # Write the captured data to JSON file
#             with open("captured_data.json", "w") as json_file:
#                 json.dump(captured_data, json_file, indent=4)

#         # Write to the text file
#         with open("seconddata.json", "a+") as f:
#             f.write(str(r) + '\n')
        
#         await asyncio.sleep(0.1)

# asyncio.get_event_loop().run_until_complete(main())





#Final Code
import websockets
import asyncio
import json
import time
from datetime import datetime, timedelta

# ... (rest of your code remains unchanged) ...

async def capture_data(websocket, uri):
    while True:
        try:
            data = await websocket.recv()
            data = json.loads(data)
            
            try:
                last_price = data['data'][0]["lastPrice"]
                return last_price
            except KeyError:
                continue
        except:
            print("Quitting")
            return 0

async def main():
    captured_data = []  # Create an empty list to hold the captured data
    captured_holc = []  # Create an empty list to hold the HOLC data
    last_capture_time = datetime.now()

    switchh = 0
    uri = "wss://www.bitmex.com/realtime?subscribe=instrument:XBTUSD"
    while switchh == 0:
        try:
            websocket = await websockets.connect(uri)
            switchh = 1
            print("\nConnected")
        except:
            print("\nCould not Connect. Retrying in 5 seconds")
            await asyncio.sleep(5)
            continue

    while True:
        r = await asyncio.create_task(capture_data(websocket, uri))
        if r == 0:
            try:
                websocket = await websockets.connect(uri)
                print("Connected")
            except:
                print("Reconnection failed. Retrying in 5 seconds")
            await asyncio.sleep(5)
            continue
    
        print(r, end='\n')

        # Check if a minute has passed since the last capture
        current_time = datetime.now()
        if current_time - last_capture_time >= timedelta(minutes=1):
            captured_data.append({"timestamp": current_time.timestamp(), "last_price": r})
            last_capture_time = current_time

            # Extract the HOLC values
            if captured_data:
                open_price = captured_data[0]["last_price"]
                close_price = captured_data[-1]["last_price"]
                high_price = max([item["last_price"] for item in captured_data])
                low_price = min([item["last_price"] for item in captured_data])
                captured_holc.append({
                    "timestamp": current_time.timestamp(),
                    "open_price": open_price,
                    "high_price": high_price,
                    "low_price": low_price,
                    "close_price": close_price
                })
            
            # Write the captured data to JSON file
            with open("captured_data.json", "w") as json_file:
                json.dump(captured_data, json_file, indent=4)
            
            # Write the HOLC data to JSON file
            with open("captured_holc.json", "w") as json_file:
                json.dump(captured_holc, json_file, indent=4)
                
            # Use the closing price of the current minute as the opening price of the next minute
            # next_open_price = close_price
            # captured_holc = [{"timestamp": current_time.timestamp(), "last_price": next_open_price}]
            # captured_holc = []

        # Write to the text file
        with open("seconddata.json", "a+") as f:
            f.write(str(r) + '\n')
        
        await asyncio.sleep(0.1)

asyncio.get_event_loop().run_until_complete(main())









