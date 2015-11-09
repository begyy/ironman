from zope.interface import Interface, Attribute

class IPacketStorage(Interface):
    """ Basic enhanced dictionary to centrally manage all packet data
    """

    def record(packet):
        """ record the packet
        """

class IHistory(Interface):
    """ Enhanced dictionary to store inbound and outbound packet pairs
    """

    def record(inbound_packet, outbound_packet):
        """ record both packets
        """

class IIPBusPacket(Interface):
    """ IPBus Packet object
    """
    _blob = Attribute("The data blob that this packet corresponds to")
    littleendian = Attribute("A flag dictating whether the datagram is received/sent in little-endian.")
    struct = Attribute("The C-type struct representation of the packet.")
    raw = Attribute("The raw datagram blob.")
    blob = Attribute("The big-endian datagram blob.")
    protocol_version = Attribute("The packet header protocol version. This does not check that the encapsulated transactions also match.")
    reserved = Attribute("Reserved. Should be 0x0.")
    packet_id = Attribute("The id of the ipbus packet.")
    byteorder = Attribute("The byte-order in the header. Should assert == 0xf.")
    packet_type = Attribute("""The type of packet.

            ======= ===============
            Value   Type
            ======= ===============
            0x0     Control
            0x1     Status
            0x2     Re-send request
            0x3-f   Reserved
            ======= ===============""")


    def __init__(blob):
        """ Packet is initialized with a data blob
            to decode. Determine if it is big or little endian.
        """

    def __eq__(other):
        """ Define a way to identify two packets as being equivalent. Best way is to compare the underlying structs
        """

    def __ne__(other):
        """ This should just be :code:`return not self.__eq__(other)`.
        """

class IHardwareManager(Interface):
    """ Our Hardware Maps manager
    """
    def check_data(address, data):
        """ Given an address, checks if the data is
            a valid value to write
        """

    def check_address(address):
        """ Given an address, checks if it is valid
        """

    def find_address(address):
        """ Look up an address, return Error if cannot find
        """

    def get_checksum(map_name):
        """ Look up the checksum for a given map name
        """

    def add(hw_map):
        """ Add the Map object to the Hardware
        """

class IHardwareMap(Interface):
    """ Manages information about a single map, should be an overloaded dictionary
    """
    doc = Attribute("The parsed XML document, effectively a dictionary whose keys are addressses and values are :class:`INode` objects.")

    def __init__(xml):
        """ Initialize a hardware map object by giving it the data to parse
        """

    def parse(xml):
        """ Parse the xml hardware map data to set things up
        """

    def isOk():
        """ Whether or not the given hardware map is ok. Should just be a loop over :func:`IHardwareNode.isOk`.
        """

class IHardwareNode(Interface):
    """ Manages information about a single address. Simply a well-defined dictionary.
    """
    #description = Attribute("A description of the node.")
    permissions = Attribute("Mark the node's read/write capabilities.")
    allowed = Attribute("A list of allowed values for the node.")
    disallowed = Attribute("A list of disallowed values for the node.")
    readable = Attribute("Is the given node readable?")
    writeable = Attribute("Is the given node writeable?")
    isOk = Attribute("Is the given node ok? EG: can't set allowed and disallowed objects at the same time and cannot block a node from being readable.")

    def __init__(node):
        """ Initialize the node by giving it the parsed xml data
        """

    def isValueValid(val):
        """ Whether the given value is a valid value for the node
        """

class ICommunicationSlave(Interface):
    """ Manages the communication with the programmable logic for us
    """
    def parse_address(address):
        """ Parses address and returns what function to call
        """

    def __call__(packet):
        """ A non-blocking I/O call passing along the packet
        """
