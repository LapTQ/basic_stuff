import os
import datetime

CLIENT_PATH = "/home/ad/Workspace/trivial_projects/Internet_application/clients/"

class Package:
    """Represent a package."""
    
    def __init__(self, A, location='', label=datetime.datetime.now().strftime("%Y%m%d%H%M%S"), B=None):
        """
        Create a new package.
        
        A           the owner or sender
        B           the receiver (default None)
        """
        self._A = A
        self._label = label
        self._B = B
        self._location = location
        self._opened = False
        
        self._box = open(location + label, "a")
        self._box.close()
 
        
    def _check_opened(self):
        """Return True if package is opened, False otherwise."""
        return self._opened
    
    def _mark_opened(self):
        """Mark package as opened."""
        self._opened = True
        
    def _mark_unopened(self):
        """Mark package as unopended."""
        self._opened = False
        
    def _get_label(self):
        """Return label of the package."""
        return self._label
        
    def _set_label(self, label):
        """Set another label for the package."""
        self._label = label
        
    def _get_A(self):
        """Return the name of the owner of the package."""
        return str(self._A)
        
    def _get_B(self):
        """Return the name of the receiver of the package."""
        return str(self._B)
        
    def _set_B(self, B):
        """Set the receiver of the package."""
        self._B = B
        
    def _get_location(self):
        """Return the current location of the package."""
        return self._location
        
    def _set_location(self, location):
        """Set new upcoming location for the package."""
        self._location = location
        
    def _open(self, mode="a"):
        """Open package."""
        self._mark_opened()
        return open(self._location + self._label, mode)
        
    def _close(self):
        """Close package."""
        return self._box.close()
        
    def __str__(self):
        """Return string representation of package."""
        return self._location + '/' + self._label
    
   
class Delivery(Package):
    """An application that sends packages between parties."""
    
    def __init__(self, A, B, label=datetime.datetime.now().strftime("%Y%m%d%H%M%S")):
        """
        Run an application that sends packages.
        
        A       client who calls sending request
        B       client who receives letter
        """
        super().__init__(A, A._get_path() + "/outbox/", label, B)
              
    def _open(self, mode="a"):
        """Open package."""
        self._mark_opened()
        new_location = self._A._get_path() + "/draft/"
        os.rename(str(self), new_location + self._get_label())
        self._set_location(new_location)
        return open(str(self), mode)
    
    def _close(self):
        """Close package and move it to outbox."""
        super()._close()
        new_location = self._A._get_path() + "/outbox/"
        os.rename(str(self), new_location + self._get_label())
        self._set_location(new_location)
        self._mark_unopened()
        return self._box.close()
    
    def _send(self):
        """Process of sendind letter from A's outbox to B's inbox."""
        if self._A._check_outbox(self) == False:
            print("Can't find it.")
        else:
            print(str(self._A), "------   ", "Sending", self._get_label(), ". . .", "------>   ", str(self._B))
            new_location = self._B._get_path() + "/inbox/"
            os.rename(str(self), new_location + self._get_label())
            self._set_location(new_location)
            if self._B._check_inbox(self) == True:
                print(self._get_label(), "sent successfully.")
            else:
                raise IOError("Something went wrong.")

        
class Clients:
    """A client for Internet Application."""
    
    def __init__(self, name, ICN):
        """
        Create a mailbox for a client.
        
        name        Name of client
        ICN         Identification Card Number
        """
        self._ICN = ICN
        self._name = name
        self._path = CLIENT_PATH + self._ICN
        self._create_mailbox()
         
    def __str__(self):
        """Return string representation of client."""
        return self._ICN + ': ' + self._name
    
    def _get_ICN(self):
        """Return ICN as a ID for client."""
        return self._ICN
        
    def _get_name(self):
        """Return name of the client with a given ID."""
        return self._name
        
    def _create_mailbox(self):
        """Make a mailbox for new client."""
        os.mkdir(self._path)                             # make a client's own mailbox (eg. '132441163')
        file_info = open(self._path + "/info.txt", "w")  # file consist of information about client
        print(self._get_ICN(), file=file_info)
        print("Name:", self._get_name(), sep='', file=file_info)
        os.mkdir(self._path + "/draft")                  # make outbox directory
        os.mkdir(self._path + "/outbox")                 # make outbox directory
        os.mkdir(self._path + "/inbox")                  # make inbox directory
        os.mkdir(self._path + "/trash")                  # make trash directory

    def _get_path(self):
        """Return path of the client's main directory."""
        return self._path

    def _check_outbox(self, package):
        """Return True if there is any letter in A's outbox, False otherwise."""
        return True if "outbox" in str(package) else False
            
    def _check_inbox(self, package):
        """Return True if there is any letter in A's inbox, False otherwise."""
        return True if "inbox" in str(package) else False
                   
    def _unbox(self, package):
        """With newly received mail, ask for read."""
        open_box = open(str(package), "r")
        content = open_box.read()
        package._mark_opened()
        open_box.close()
        print(content)
        
    def _delete(self, package):
        """Delete mail with given label."""
        new_location = self._get_path() + "/trash/"
        os.rename(str(package), new_location + package._get_label())
        package._set_location(new_location)
        return "Remove successfully." if os.path.exists(str(package)) else "Remove NOT successfully"
        




    
    
    
    
    
    
