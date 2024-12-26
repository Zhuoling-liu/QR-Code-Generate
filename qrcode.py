import helper
import txtdata

class QRCode:
    '''A class that srores information about a qrcode.
    
    Attributes: file_path, last_update_date, owner, and error_correction
    '''
    def __init__(self,file_path,last_update_date = "00/00/0000",
                 owner = "Default Owner",error_correction = 0.0):
        '''
		(str, str, str, float) -> QRcode
        Create a new QRCode object with the given file_path, 
        last_update_date, owner, and error_correction.

        >>> my_qrcode = QRCode("your_qrcode.txt","01/09/2024","Vivian",0.1)
        >>> my_qrcode.last_update_date['Day']
        '01'
        >>> my_qrcode.last_update_date['Month']
        '09'
        >>> my_qrcode.last_update_date['Year']
        '2024'
        >>> my_qrcode.owner
        'Vivian'
        >>> my_qrcode.error_correction
        0.1
        
        >>> my_qrcode2 = QRCode("pretty_save.txt")
        >>> my_qrcode2.last_update_date['Day']
        '00'
        >>> my_qrcode2.owner
        'Default Owner'
        >>> my_qrcode2.error_correction
        0.0
        
        >>> my_qrcode3 = QRCode("my_qrcode.txt", "15/04/2023", "John Doe", 0.2)
        >>> my_qrcode3.last_update_date['Day']
        '15'
        >>> my_qrcode3.last_update_date['Month']
        '04'
        >>> my_qrcode3.last_update_date['Year']
        '2023'
        >>> my_qrcode3.owner
        'Jolin'
        >>> my_qrcode3.error_correction
        0.2
        '''
        date_dict = helper.convert_date(last_update_date)
        my_list = helper.get_data(file_path)
        self.last_update_date = date_dict
        self.owner = owner
        self.data = txtdata.TxtData(my_list)
        self.error_correction =error_correction
     
    def __str__(self):
        '''
		() -> str
        
		>>> my_qrcode = QRCode("your_qrcode.txt", "01/09/2024", "Vivian", 0.1)
		>>> print(my_qrcode)
		The QR Code was created by Vivian and last updated in 2024.
		The details regarding the QR code file are as follows:
		This TxtData object has 6 rows and 9 columns.

		>>> my_qrcode2 = QRCode("my_qrcode.txt", "15/04/2023", "John Doe", 0.2)
		>>> print(my_qrcode2)
		The QR Code was created by John Doe and last updated in 2023.
		The details regarding the QR code file are as follows:
		This TxtData object has 3 rows and 11 columns.

        >>> my_qrcode2 = QRCode("test_code.txt", "15/01/2023", "John Doe", 0.2)
		>>> print(my_qrcode2)
		The QR Code was created by John Doe and last updated in 2023.
		The details regarding the QR code file are as follows:
		This TxtData object has 2 rows and 4 columns.
		'''
        return 'The QR code was created by ' + self.owner + \
                ' and last updated in ' + self.last_update_date['Year'] + \
            '.\nThe details regarding the QR code file are as follows:\n' + \
            'This TxtData object has ' + str(self.data.rows) + ' rows and ' + \
            str(self.data.cols) + ' columns.' 

    def equals(self,another_qrcode):
        '''
        (QRCode) -> bool
        Determine if the two QRCodes are the same.

        >>> qrcode1 = QRCode("my_qrcode.txt", "01/09/2024", "Vivian", 0.1)
        >>> qrcode2 = QRCode("my_qrcode.txt", "01/09/2024", "Vivian", 0.1)
        >>> qrcode1.equals(qrcode2)
        True

        >>> qrcode3 = QRCode("qrcode_binary.txt", "15/04/2023", "John Doe", 0.7)
        >>> qrcode4 = QRCode("qrcode_binary.txt", "15/04/2023", "John Doe", 0.2)
        >>> qrcode3.equals(qrcode4)
        False

        >>> qrcode5 = QRCode("qrcode_binary.txt", "01/09/2024", "Vivian", 0.1)
        >>> qrcode6 = QRCode("qrcode_binary_copy.txt",
        "01/09/2024", "Vivian", 0.1)
        >>> qrcode6.equals(qrcode5)
        True
        '''
        # Check if the error correction and data are the same in both QR codes
        if self.error_correction == another_qrcode.error_correction and \
        self.data.data == another_qrcode.data.data:
            return True
        return False

    
    def is_corrupted(self,precise_qrcode):
        '''
        (QRCode) -> bool
        Determine if the self object is corrupted.

        >>> qrcode1 = QRCode("test_qrcode_copy.txt",
        "01/09/2024", "Vivian", 0.1)
        >>> precise_qrcode = QRCode("test_code_copy.txt",
        "01/09/2024", "Vivian", 0.0)
        >>> qrcode1.is_corrupted(precise_qrcode)
        False

        >>> qrcode2 = QRCode("qrcode_pretty.txt",
        "01/09/2024", "Vivian", 0.05)
        >>> precise_qrcode2 = QRCode("your_qrcode.txt",
        "01/09/2024", "Vivian", 0.0)
        >>> qrcode2.is_corrupted(precise_qrcode2)
        True

        >>> qrcode3 = QRCode("qrcode_binary.txt", "15/04/2023", "John Doe", 0.2)
        >>> precise_qrcode3 = QRCode("qrcode_binary_copy.txt",
        "15/04/2023", "John Doe", 0.2)
        >>> qrcode3.is_corrupted(precise_qrcode3)
        False
        '''
        # Compare the QRcode to check 
        #if their difference is under error correction.
        return not self.data.approximately_equals(precise_qrcode.data, 
                                                    self.error_correction)
       


