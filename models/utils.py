import typesentry

tc_check = typesentry.Config().is_type

def force_type(*types):
	def decorator(func):
		def wrapper(*args, **kwargs):
			from pda import State

			for arg, enforced_type in zip(args[1:], types):
				if not tc_check(arg, enforced_type):
					raise Exception(f"Bad Type {arg} {enforced_type}")
			return func(*args, **kwargs)

		return wrapper
	return decorator