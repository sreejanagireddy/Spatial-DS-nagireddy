	Mongo db : world_data

•	collections:

1.airports
2.earthquakes
3.meteorite
4.state_borders
5.volcanos

Example queries:

•	Query 1 :

  1.   python query1.py LAX CIA 1000
  2.   python query1.py IAD RUH 1000
  3.   python query1.py CAI YUL 1000
  
•	Query 2 :

1.	python query2.py [138.252924,36.204824] 1000
2.	python query2.py meteorite mass 800 min 10 1000 [138.252924,36.204824]
3.	python query2.py volcanos altitude 1000 min 2 1000 [138.252924,36.204824]
4.	 python query2.py earthquakes mag 8 min 5 1000 [138.252924,36.204824]

•	Query 3

1.python query3.py volcanos 5 20
2.python query3.py earthquakes 5 20
3.python query3.py meteorite 5 20



