def filterArrayByKey (array, key, value):
	return list(
		filter(
			lambda member: compare(member, key, value),
			array
		)
	)

def compare(object, key, value):
	return object[key] == value