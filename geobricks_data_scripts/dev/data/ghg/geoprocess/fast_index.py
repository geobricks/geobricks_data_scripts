import shapefile
import shapely

#Load the shapefile of polygons and convert it to shapely polygon objects
polygons_sf = shapefile.Reader("C:/PolygonShapeFile.shp")
polygon_shapes = polygons_sf.shapes()
polygon_points = [q.points for q in polygon_shapes ]
from shapely.geometry import Polygon
polygons = [Polygon(q) for q in polygon_points]

#Load the shapefile of points and convert it to shapely point objects
points_sf = shapefile.Reader("C:/PointShapeFile.shp")
point_shapes = points_sf.shapes()
from shapely.geometry import Point
point_coords= [q.points[0] for q in point_shapes ]
points = [Point(q.points[0]) for q in point_shapes ]

#Build a spatial index based on the bounding boxes of the polygons
from rtree import index
idx = index.Index()

count = -1
for q in polygon_shapes:
    count +=1
    idx.insert(count, q.bbox)

#Assign one or more matching polygons to each point
matches = []
for i in range(len(points)): #Iterate through each point
    temp= None
    print "Point ", i
    #Iterate only through the bounding boxes which contain the point
    for j in idx.intersection( point_coords[i]):
        #Verify that point is within the polygon itself not just the bounding box
        if points[i].within(polygons[j]):
            print "Match found! ",j
            temp=j
            break
    matches.append(temp) #Either the first match found, or None for no matches