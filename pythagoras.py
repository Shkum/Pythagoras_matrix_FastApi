class Pythagoras:
    def __init__(self, b_day, b_month, b_year):
        self.variables = {}
        self.b_day = b_day
        self.b_month = b_month
        self.b_year = b_year
        self.nums = self.get_pythagoras()

    def get_pythagoras(self):
        calc_str = (self.b_day + self.b_month + self.b_year).replace('0', "")
        first_num = sum(map(int, calc_str))
        second_num = sum(map(int, str(first_num)))
        third_num = first_num - int(self.b_day.lstrip('0')[0]) * 2
        forth_num = sum(map(int, str(third_num)))
        final_string = (calc_str + str(first_num) + str(second_num) + str(third_num) + str(forth_num)).replace('0', '')

        self.variables['embodiment'] = len(final_string)
        self.variables['first_num'] = first_num
        self.variables['second_num'] = second_num
        self.variables['third_num'] = third_num
        self.variables['forth_num'] = forth_num
        self.variables['first_line'] = 0
        self.variables['second_line'] = 0
        self.variables['third_line'] = 0
        self.variables['first_col'] = 0
        self.variables['second_col'] = 0
        self.variables['third_col'] = 0
        self.variables['diagonal_down'] = 0
        self.variables['diagonal_up'] = 0

        nums = []
        for i in range(1, 10):
            num = final_string.count(str(i)) * str(i)
            nums.append(num)

            if i == 1 or i == 4 or i == 7:
                self.variables['first_line'] += len(num)
            if i == 2 or i == 5 or i == 8:
                self.variables['second_line'] += len(num)
            if i == 3 or i == 6 or i == 9:
                self.variables['third_line'] += len(num)
            if i == 1 or i == 2 or i == 3:
                self.variables['first_col'] += len(num)
            if i == 4 or i == 5 or i == 6:
                self.variables['second_col'] += len(num)
            if i == 7 or i == 8 or i == 9:
                self.variables['third_col'] += len(num)
            if i == 1 or i == 5 or i == 9:
                self.variables['diagonal_down'] += len(num)
            if i == 3 or i == 5 or i == 7:
                self.variables['diagonal_up'] += len(num)

        return nums
