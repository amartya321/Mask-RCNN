class KangarooDataset(Dataset):
	def load_dataset(self,dataset_dir,is_train=True):
		self.add_class('dataset',1,'kangaroo')
		images_dir = dataset_dir+ '/images/'
		annotations_dir = dataset_dir+ '/annots/'
		for filename in listdir(images_dir):
			image_id=filename[:-4]
			if image_id in ['00090']:
				continue
			if is_train and int(image_id)>=150:
				continue
			if not is_train and int(image_id)<150:
				continue
			img_path =	images_dir + filename
			ann_path = annotations_dir + image_id +'.xml'
			self.add_image('dataset',image_id=image_id,path=img_path,annotation=ann_path)	
		