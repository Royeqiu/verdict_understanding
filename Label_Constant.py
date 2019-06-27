
model_path = '../model/'
is_labeled = 'fcs_29'
vector_len = 18

alcohol_code = 'fcs_33'
alcohol_context = 'fcs_33_context'
alcohol_vec_len = 7
alcohol_vec_index = 0
alcohol_key_words = ['毫克']
alcohol_max_len = 0
alcohol_threshold = 0
alcohol_is_ml_model = False

vehicle_code = 'fcs_34'
vehicle_context = 'fcs_34_context'
vehicle_vec_len = 3
vehicle_vec_index = 7
vehicle_key_words = ['機車','小客貨車','小客車','大型車']
vehicle_model_name = 'vehicle.h5'
vehicle_max_len = 309
vehicle_threshold = 0
vehicle_is_ml_model = True

region_code = 'fcs_35'
region_context = 'fcs_35_context'
region_vec_len = 4
region_vec_index = 10
region_key_words = ['巷','弄','縣','市']
region_model_name = 'region.h5'
region_max_len = 100
region_threshold = 0
region_is_ml_model = True


accident_code = 'fcs_36'
accident_context = 'fcs_36_context'
accident_vec_len = 1
accident_vec_index = 14
accident_key_words = ['發生損害','損害','受傷','傷害']
accident_threshold = 0.8
accident_model_name = 'accident.h5'
accident_max_len = 137
accident_is_ml_model = True

violate_property_code = 'fcs_38'
violate_property_context = 'fcs_38_context'
violate_property_vec_len = 1
violate_property_vec_index = 15
violate_property_key_words = [ '多人','車禍當事人','致重傷者','擦撞']
violate_max_len = 0
violate_threshold = 0
violate_is_ml_model = False

driving_occupation_code = 'fcs_41'
driving_occupation_context = 'fcs_41_context'
driving_occupation_vec_len = 1
driving_occupation_vec_index = 16
driving_occupation_key_words = ['其業務', '職業']
driving_occupation_threshold = 0.5
driving_occupation_model_name = 'driving_occupation.h5'
driving_occupation_max_len = 154
driving_occupation_is_ml_model = True

commit_crime_code = 'fcs_42'
commit_crime_context = 'fcs_42_context'
commit_crime_vec_len = 1
commit_crime_vec_index = 17
commit_crime_key_words = ['坦承', '直承']
commit_crime_threshold = 0.2
commit_crime_model_name = 'commit_crime.h5'
commit_crime_max_len = 154
commit_crime_is_ml_model = True


factor_code_list = [alcohol_code,vehicle_code,region_code,accident_code,violate_property_code,driving_occupation_code,commit_crime_code]
factor_key_words_list = [alcohol_key_words,vehicle_key_words,region_key_words,accident_key_words,violate_property_key_words,driving_occupation_key_words,commit_crime_key_words]
factor_max_len_list = [alcohol_max_len,vehicle_max_len,region_max_len,accident_max_len,violate_max_len,driving_occupation_max_len,commit_crime_max_len]
factor_threshold_list = [alcohol_threshold, vehicle_threshold, region_threshold, accident_threshold, violate_threshold, driving_occupation_threshold, commit_crime_threshold]
factor_vec_len_list = [alcohol_vec_len,vehicle_vec_len,region_vec_len,accident_vec_len,violate_property_vec_len,driving_occupation_vec_len,commit_crime_vec_len]
factor_is_ml_model_list = [alcohol_is_ml_model, vehicle_is_ml_model, region_is_ml_model,accident_is_ml_model, violate_is_ml_model, driving_occupation_is_ml_model, commit_crime_is_ml_model]