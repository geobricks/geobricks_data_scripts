from geobricks_data_scripts.demo.old_ghg.utils.data_manager_util import get_data_manager


data_manager = get_data_manager()


data_manager.delete("ghg:organic_soil_surface_area")

# def delete_uid(uid):
#     try:
#         data_manager.delete_coveragestore(uid, True, True)
#     except Exception, e:
#         print "ERROR delete_uid: ", e
#
# uids = ["ghg@cattle10km_ad_-_2010", "ghg@sheep10km_ad_-_2010"]
# for uid in uids:
#    delete_uid(uid)



# layers = data_manager.metadata_manager.get_all_layers()
# for layer in layers:
#     try:
#         print layer["uid"]
#         #data_manager.delete_coveragestore(layer["uid"], True, True)
#         data_manager.metadata_manager.delete_metadata(layer["uid"])
#     except Exception, e:
#         print "ERROR: deleting ", e
#         pass


# delete maghg
# with open('../coding_systems/csv/cs_maghg.csv', 'rb') as csvfile:
#     rows = csv.reader(csvfile)
#     for row in rows:
#         print row
        #data_manager.delete_coveragestore("ghg:"+row[0])
        # print data_manager.metadata_manager.get_by_uid("ghg:"+row[0])

