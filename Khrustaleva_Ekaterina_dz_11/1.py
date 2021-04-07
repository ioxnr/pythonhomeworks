class Date:
    def __init__(self, my_date):
        self.my_date = str(my_date)
        new_date = Date.extraction(self.my_date)
        print('Date:', new_date['date'])
        print('Month:', new_date['month'])
        print('Year:', new_date['year'])
        print(Date.validate(new_date))

    @classmethod
    def extraction(cls, my_date):
        date, month, year = map(int, my_date.split('-'))
        return {'date': date, 'month': month, 'year': year}

    @staticmethod
    def validate(data):
        if 0 < data['date'] <= 31:
            if 0 < data['month'] <= 12:
                if 0 < data['year'] <= 2020:
                    return 'Everything is right'
                return 'Wrong year'
            return 'Wrong month'
        return 'Wrong date'


today = Date('07-04-2021')
day = Date('32-06-2016')
second_day = Date('16-78-2009')
third_day = Date('08-12-2030')
