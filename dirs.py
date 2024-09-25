import os

def list_subdirectories(path):
  """Lists all subdirectories within the given path.

  Args:
      path: The directory path.

  Returns:
      A list of subdirectory names.
  """
  with os.scandir(path) as entries:
    return [entry.name for entry in entries if entry.is_dir()]

# Example usage
input_dir = "/Volumes/WyDrive_MIA/videos/tv"
subdirectories = list_subdirectories(input_dir)

tv_list = []

print("Subdirectories:")
for subdir in subdirectories:
  print(subdir)
  tv_list.append(subdir)

input_dir = "/Volumes/WyDrive_NRT/tv"
subdirectories = list_subdirectories(input_dir)

nrt_tv_list = []

print("NRT Subdirectories:")
for subdir in subdirectories:
  print(subdir)
  nrt_tv_list.append(subdir)

print(nrt_tv_list)

def diff_using_sets(arr1, arr2):
  set1 = set(arr1)
  set2 = set(arr2)
  difference1 = set1.difference(set2)  # Elements in arr1 but not arr2
  difference2 = set2.difference(set1)  # Elements in arr2 but not arr1
  return difference1, difference2

# Example usage

diff1, diff2 = diff_using_sets(tv_list, nrt_tv_list)
print(type(diff1))

print("\nElements in MIA but not in NRT:", sorted(diff1))
print("\nElements in NRT but not MIA:", diff2)
