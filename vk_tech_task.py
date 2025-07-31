def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    num2_set = set(nums2)
    intersection_num = filter(lambda x: x in num2_set, nums1)
    return list(set(intersection_num))
