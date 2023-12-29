genres = ['Action', 'Comedy', 'Drama', 'Fantasy', 'Horror', 'Romance', 'Sci-Fi', 'Thriller', 'Documentary', 'Animation']

movie_data = [
    ['Romance', 'Golden Legacy', 'Guillermo del Toro', 2023, '4.2'],
    ['Thriller', 'Eternal Revenge', 'Sofia Coppola', 2009, '4.6'],
    ['Animation', 'Eternal Legacy', 'Patty Jenkins', 2004, '3.9'],
    ['Horror', 'Eternal Light', 'Sofia Coppola', 1981, '2.0'],
    ['Drama', 'Distant Empire', 'Jordan Peele', 1982, '4.4'],
    ['Drama', 'Distant Vision', 'Martin Scorsese', 1996, '3.1'],
    ['Action', 'Eternal Secret', 'Patty Jenkins', 2004, '1.3'],
    ['Sci-Fi', 'Dark Journey', 'Steven Spielberg', 1982, '3.9'],
    ['Sci-Fi', 'Last Vision', 'Martin Scorsese', 2019, '3.6'],
    ['Fantasy', 'Last Heart', 'Christopher Nolan', 1986, '2.6'],
    ['Comedy', 'Hidden Shadow', 'Jordan Peele', 1999, '4.7'],
    ['Documentary', 'Golden Shadow', 'Sofia Coppola', 2022, '2.3'],
    ['Drama', 'Hidden Dream', 'Greta Gerwig', 1984, '1.3'],
    ['Romance', 'Mysterious Revenge', 'Steven Spielberg', 1994, '4.4'],
    ['Drama', 'Broken Journey', 'Kathryn Bigelow', 1982, '3.1'],
    ['Horror', 'Mysterious Empire', 'Patty Jenkins', 2006, '1.7'],
    ['Romance', 'Eternal Secret', 'Jordan Peele', 2004, '2.5'],
    ['Action', 'Distant Vision', 'Jordan Peele', 1980, '4.8'],
    ['Horror', 'Silent Light', 'Steven Spielberg', 1995, '2.0'],
    ['Documentary', 'Hidden Shadow', 'James Cameron', 2004, '2.6'],
    ['Horror', 'Last Secret', 'Greta Gerwig', 1989, '5.0'],
    ['Drama', 'Golden Journey', 'Steven Spielberg', 2019, '3.1'],
    ['Romance', 'Broken Dream', 'Greta Gerwig', 2012, '3.8'],
    ['Sci-Fi', 'Hidden Shadow', 'Steven Spielberg', 2012, '3.1'],
    ['Comedy', 'Distant Journey', 'Jordan Peele', 2015, '3.6'],
    ['Sci-Fi', 'Golden Revenge', 'Steven Spielberg', 2021, '4.6'],
    ['Fantasy', 'Last Secret', 'Jordan Peele', 2012, '2.1'],
    ['Documentary', 'Distant Empire', 'Jordan Peele', 1988, '2.8'],
    ['Thriller', 'Dark Revenge', 'Greta Gerwig', 1993, '3.1'],
    ['Fantasy', 'Silent Shadow', 'Steven Spielberg', 1996, '4.6'],
    ['Documentary', 'Hidden Empire', 'Christopher Nolan', 2018, '4.0'],
    ['Horror', 'Last Dream', 'Guillermo del Toro', 2011, '5.0'],
    ['Comedy', 'Distant Heart', 'James Cameron', 2023, '1.4'],
    ['Action', 'Distant Heart', 'Christopher Nolan', 2008, '3.5'],
    ['Romance', 'Broken Dream', 'Patty Jenkins', 2012, '2.6'],
    ['Drama', 'Golden Shadow', 'Sofia Coppola', 1996, '4.8'],
    ['Action', 'Lost Shadow', 'James Cameron', 1995, '2.4'],
    ['Romance', 'Silent Journey', 'Guillermo del Toro', 2015, '4.9'],
    ['Romance', 'Eternal Legacy', 'Christopher Nolan', 1991, '4.5'],
    ['Horror', 'Last Vision', 'Steven Spielberg', 2008, '2.6'],
    ['Romance', 'Hidden Shadow', 'James Cameron', 1999, '2.0'],
    ['Horror', 'Silent Vision', 'Martin Scorsese', 1997, '1.9'],
    ['Action', 'Hidden Dream', 'Patty Jenkins', 2015, '4.6'],
    ['Action', 'Hidden Vision', 'Sofia Coppola', 2019, '2.6'],
    ['Animation', 'Silent Secret', 'James Cameron', 2010, '4.5'],
    ['Comedy', 'Last Heart', 'Martin Scorsese', 1980, '3.5'],
    ['Fantasy', 'Lost Light', 'Greta Gerwig', 1988, '1.5'],
    ['Comedy', 'Golden Shadow', 'Patty Jenkins', 2018, '1.2'],
    ['Documentary', 'Distant Legacy', 'Kathryn Bigelow', 2007, '2.5'],
    ['Horror', 'Lost Journey', 'Martin Scorsese', 2015, '2.1'],
    ['Documentary', 'Distant Revenge', 'Jordan Peele', 2009, '2.9'],
    ['Horror', 'Silent Shadow', 'Greta Gerwig', 1997, '4.0'],
    ['Comedy', 'Last Secret', 'Christopher Nolan', 2016, '2.3'],
    ['Sci-Fi', 'Broken Empire', 'Patty Jenkins', 2000, '4.5'],
    ['Thriller', 'Silent Journey', 'Patty Jenkins', 1983, '3.1'],
    ['Horror', 'Eternal Vision', 'James Cameron', 2005, '3.5'],
    ['Sci-Fi', 'Mysterious Revenge', 'Martin Scorsese', 1980, '2.3'],
    ['Fantasy', 'Broken Journey', 'Patty Jenkins', 2021, '4.0'],
    ['Animation', 'Eternal Heart', 'James Cameron', 2014, '2.3'],
    ['Fantasy', 'Mysterious Journey', 'Christopher Nolan', 1989, '3.8'],
    ['Horror', 'Silent Vision', 'Steven Spielberg', 2011, '3.6'],
    ['Documentary', 'Broken Shadow', 'Guillermo del Toro', 1986, '3.8'],
    ['Horror', 'Distant Vision', 'Steven Spielberg', 1998, '3.3'],
    ['Horror', 'Hidden Legacy', 'Martin Scorsese', 2001, '2.5'],
    ['Comedy', 'Broken Journey', 'Sofia Coppola', 1982, '3.4'],
    ['Romance', 'Last Journey', 'Kathryn Bigelow', 1991, '4.1'],
    ['Sci-Fi', 'Last Legacy', 'Christopher Nolan', 2010, '4.6'],
    ['Romance', 'Last Vision', 'Sofia Coppola', 2012, '2.9'],
    ['Documentary', 'Broken Empire', 'Greta Gerwig', 2013, '3.9'],
    ['Documentary', 'Dark Legacy', 'Patty Jenkins', 2005, '3.7'],
    ['Documentary', 'Dark Shadow', 'Greta Gerwig', 2023, '1.7'],
    ['Animation', 'Dark Dream', 'Steven Spielberg', 2000, '3.5'],
    ['Sci-Fi', 'Golden Heart', 'James Cameron', 1984, '1.5'],
    ['Horror', 'Distant Dream', 'Patty Jenkins', 2012, '1.9'],
    ['Comedy', 'Silent Light', 'Jordan Peele', 2005, '2.9'],
    ['Thriller', 'Mysterious Revenge', 'Sofia Coppola', 2002, '2.8'],
    ['Documentary', 'Silent Light', 'Kathryn Bigelow', 1987, '1.2'],
    ['Documentary', 'Broken Legacy', 'Martin Scorsese', 2002, '2.4'],
    ['Comedy', 'Golden Shadow', 'Sofia Coppola', 2017, '4.0'],
    ['Romance', 'Broken Secret', 'James Cameron', 1995, '4.7'],
    ['Romance', 'Golden Light', 'James Cameron', 2018, '3.9'],
    ['Comedy', 'Hidden Journey', 'James Cameron', 2004, '1.0'],
    ['Comedy', 'Lost Heart', 'Martin Scorsese', 1982, '3.6'],
    ['Horror', 'Last Empire', 'Patty Jenkins', 1998, '4.0'],
    ['Documentary', 'Distant Empire', 'Kathryn Bigelow', 2020, '3.1'],
    ['Action', 'Dark Revenge', 'Jordan Peele', 2001, '3.0'],
    ['Horror', 'Mysterious Legacy', 'Steven Spielberg', 2004, '3.1'],
    ['Horror', 'Last Dream', 'James Cameron', 2014, '2.0'],
    ['Documentary', 'Eternal Light', 'Patty Jenkins', 1982, '1.8'],
    ['Horror', 'Dark Legacy', 'Martin Scorsese', 2000, '4.2'],
    ['Sci-Fi', 'Hidden Shadow', 'Patty Jenkins', 2020, '3.4'],
    ['Romance', 'Mysterious Shadow', 'Steven Spielberg', 2017, '4.7'],
    ['Horror', 'Mysterious Legacy', 'James Cameron', 2005, '1.9'],
    ['Comedy', 'Distant Light', 'Guillermo del Toro', 1996, '3.7'],
    ['Sci-Fi', 'Golden Empire', 'Steven Spielberg', 2021, '3.7'],
    ['Horror', 'Mysterious Journey', 'James Cameron', 2015, '3.8'],
    ['Comedy', 'Dark Dream', 'James Cameron', 1993, '1.0'],
    ['Action', 'Lost Vision', 'Steven Spielberg', 2018, '4.5'],
    ['Sci-Fi', 'Broken Shadow', 'Guillermo del Toro', 1984, '2.8'],
    ['Thriller', 'Hidden Vision', 'Patty Jenkins', 2000, '4.7'],
]