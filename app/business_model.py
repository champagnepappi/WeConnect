businesses = []

class Business:
    """
    This class contains methods for manipulating business
    data
    """
    def __init__(self):
        self.businesses = businesses
        self.bs = {}

    def create_business(self,title,description, category,location):
        """
        This method takes business input from user and
        appends the information to business list
        """
        self.bs['bs_id'] = len(self.businesses)+1
        self.bs['title'] = title
        self.bs['location'] = location
        self.bs['category'] = category
        self.bs['description'] = description
        businesses.append(self.bs)
        return self.bs
