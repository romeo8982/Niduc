class BitCounter:

    list_of_ones = []
    list_of_zeros = []

    def __init__(self, str_of_byte):
        ones_in_row = 0
        zeros_in_row = 0
        for b in str_of_byte:
            if bin(b).count('1'):
                if zeros_in_row != 0:
                    self.list_of_zeros.append(zeros_in_row)
                    zeros_in_row = 0
                ones_in_row += 1
            else:
                if ones_in_row != 0:
                    self.list_of_ones.append(ones_in_row)
                    ones_in_row = 0
                zeros_in_row += 1
