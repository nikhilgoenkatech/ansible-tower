import sys
import requests
import threading

######################################################################################
#                      Run the load-tests on the endpoint                            #
######################################################################################
def load_test(port, test_hostname):
  try:
    endpoint='/api/users'
    http_req = "http://" + test_hostname + ":" + str(port) + endpoint
    print(http_req)

    rsp = requests.get(http_req)
    if rsp.status_code != 200:
      print("No URL for /api/users ...." + str(e))

  except Exception as e:
    print ("Encountered exception while running load-test", e)


######################################################################################
#                      Create load-test                                              #
######################################################################################
if __name__=="__main__":
   try:
     #Configure the number of requests you want to execute on your endpoint
     no_of_requests = 1000

     if (len (sys.argv) < 2):
       print ("Please pass two arguments - IP followed by the NodePort where the application is running..")
       exit(1)

     #test_hostname would your application hosted
     hostIP = sys.argv[1]

     #Node Port where the application is reachable 
     port = sys.argv[2]

     #Schedule the threads
     for i in range(no_of_requests):
       request = threading.Thread(target=load_test, args=(port, hostIP))
       request.start()

   except Exception as e:
     print ("Encountered exceptoin while running load-test", e)


   finally:
     print ("Load test executed succesfully..")
