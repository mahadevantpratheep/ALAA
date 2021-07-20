 
def profile_pic_path(instance, filename):
	return 'Nomineefiles/{0}/{1}'.format(instance.app_id, "profile_pic.jpeg")

def distinction_file_path(instance, filename):
	return 'Nomineefiles/{0}/{1}'.format(instance.app_id, "distinction_file.pdf")

def prof_contri_papers_file_path(instance, filename):
	return 'Nomineefiles/{0}/{1}'.format(instance.app_id, "prof_contri_papers_file.pdf")

def prof_contri_patents_file_path(instance, filename):
	return 'Nomineefiles/{0}/{1}'.format(instance.app_id, "prof_contri_patents_file.pdf")

def prof_contri_membership_file_path(instance, filename):
	return 'Nomineefiles/{0}/{1}'.format(instance.app_id, "prof_contri_membership_file.pdf")

def prof_contri_books_file_path(instance, filename):
	return 'Nomineefiles/{0}/{1}'.format(instance.app_id, "prof_contri_books_file.pdf")

def prof_contri_others_file_path(instance, filename):
	return 'Nomineefiles/{0}/{1}'.format(instance.app_id, "prof_contri_others_file.pdf")

def prof_hon_award_file_path(instance, filename):
	return 'Nomineefiles/{0}/{1}'.format(instance.app_id, "prof_hon_award_file.pdf")

def nom_accom_con_file_path(instance, filename):
	return 'Nomineefiles/{0}/{1}'.format(instance.app_id, "nom_accom_con_file.pdf")

def ls1_file_path(instance, filename):
	return 'Nomineefiles/{0}/{1}'.format(instance.app_id, "ls1_file.pdf")

def ls2_file_path(instance, filename):
	return 'Nomineefiles/{0}/{1}'.format(instance.app_id, "ls2_file.pdf")

def resume_path(instance, filename):
	return 'Nomineefiles/{0}/{1}'.format(instance.app_id, "resume.pdf")

def add_file_path(instance, filename):
	return 'Nomineefiles/{0}/{1}'.format(instance.app_id, "add_file.pdf")