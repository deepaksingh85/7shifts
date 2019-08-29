"""
@author: dsingh string calculator
"""

class String_Calculator:

    def string_calculator(self,string):
        """

        Add numbers passed in the form of a delimited string of numbers.
        For example, "1,2,3" returns 6.

        Delimiters are handled in the following ways:
        - The standard delimiter is a comma `,`
        - Newlines `\n` are always acceptable with the delimiters, e.g.:
            '1\n,2\n,3'
        - Additional delimiters can be declared with the following syntax
          added before the beginning of a delimited string:
            //delim1,delim2\n
          ...then used as delimiters. For example:
            '//***,&&\n1***2&&3'
          which will be parsed to:
            1,2,3
        """
        if not isinstance(string, str):
            raise TypeError("Input must be of string type")
        if string == "":
            return 0
        string = self.normalize_custom_delimiter(string)
        if string:
            return self.sum_numbers(string.split(','))


    def normalize_custom_delimiter(self,string):
        """
        Normalise the delimiter if passed as custom
        """
        _alt_delims = '\n'
        if string.startswith('//'):
            delimiter_spec, string = string.split(_alt_delims, 1)
            delimiter_list = delimiter_spec[2:].split(',')
            for delimiter in delimiter_list:
                string = string.replace(delimiter, ',')
        return string


    def sum_numbers(self,number_list):
        result = 0
        negatives = []
        for num in number_list:
            try:
                if self.representsInt(num):
                    num = int(num)
                else:
                    continue
            except ValueError:
                raise ValueError("Input could not be converted to int")
            if num < 0:
                negatives.append(num)
            else:
                if num <= 1000:
                    result += num
        if negatives:
            raise ValueError("Negatives not allowed: {0}".format(",".join(map(str, negatives))))
        return result


    def representsInt(self,s):
        try:
            int(s)
            return True
        except ValueError:
            return False
