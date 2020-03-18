import sys
import ibm_db

hostName = ""    # IP Address Of Remote Server to BIIPOD10
database = ""         # DB name Of Remote Server
portNum = "5"             # Port Number That Receives Db2 Connections On The Remote Server 
userID = "valid_userName"           # The Instance User ID At The Remote Server
passWord = "valid_pwd" # The Password For The Instance User ID At The Remote Server
connectionID = None
sqlQuery = "select count(*) from BIIPODS.CLT_ADDRESS"

try:
    connectionID = ibm_db.connect("DATABASE="+database+";HOSTNAME="+hostName+";PORT="+portNum+";PROTOCOL=TCPIP;UID="+userID+";PWD="+passWord+";", "", "")
    if connectionID is None:
        print("Unable to connect to the \'" + hostName + "\' server.")
    else:
        stmt = ibm_db.exec_immediate(connectionID,sqlQuery)
        print("Executing sql statement")
        result = ibm_db.fetch_both(stmt)
        print("Result from DB executing Select Query:", result[0])
except Exception as ex:
       print(getattr(ex, 'message', repr(ex)))
finally:
       print("Closing Connection.....")
       ibm_db.close(connectionID)
