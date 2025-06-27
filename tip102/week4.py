# Problem A1
# def filter_sustainable_brands(brands, criterion):
#     res = []
#     for x in brands:
#         if criterion in x.get("criteria"):
#             res.append(x.get("name"))

#     return res

# brands = [
#     {"name": "EcoWear", "criteria": ["eco-friendly", "ethical labor"]},
#     {"name": "FastFashion", "criteria": ["cheap materials", "fast production"]},
#     {"name": "GreenThreads", "criteria": ["eco-friendly", "carbon-neutral"]},
#     {"name": "TrendyStyle", "criteria": ["trendy designs"]}
# ]

# brands_2 = [
#     {"name": "Earthly", "criteria": ["ethical labor", "fair wages"]},
#     {"name": "FastStyle", "criteria": ["mass production"]},
#     {"name": "NatureWear", "criteria": ["eco-friendly"]},
#     {"name": "GreenFit", "criteria": ["recycled materials", "eco-friendly"]}
# ]

# brands_3 = [
#     {"name": "OrganicThreads", "criteria": ["organic cotton", "fair trade"]},
#     {"name": "GreenLife", "criteria": ["recycled materials", "carbon-neutral"]},
#     {"name": "FastCloth", "criteria": ["cheap production"]}
# ]

# print(filter_sustainable_brands(brands, "eco-friendly"))
# print(filter_sustainable_brands(brands_2, "ethical labor"))
# print(filter_sustainable_brands(brands_3, "carbon-neutral"))

# Problem A2
# def count_material_usage(brands):
#         res = {}
#         for x in brands:
#             for y in x.get("materials"):
#                 if y not in res:
#                      res[y] = 1
#                 else:
#                      res[y] += 1

#         return res

# brands = [
#     {"name": "EcoWear", "materials": ["organic cotton", "recycled polyester"]},
#     {"name": "GreenThreads", "materials": ["organic cotton", "bamboo"]},
#     {"name": "SustainableStyle", "materials": ["bamboo", "recycled polyester"]}
# ]

# brands_2 = [
#     {"name": "NatureWear", "materials": ["hemp", "linen"]},
#     {"name": "Earthly", "materials": ["organic cotton", "hemp"]},
#     {"name": "GreenFit", "materials": ["linen", "recycled wool"]}
# ]

# brands_3 = [
#     {"name": "OrganicThreads", "materials": ["organic cotton"]},
#     {"name": "EcoFashion", "materials": ["recycled polyester", "hemp"]},
#     {"name": "GreenLife", "materials": ["recycled polyester", "bamboo"]}
# ]

# print(count_material_usage(brands))
# print(count_material_usage(brands_2))
# print(count_material_usage(brands_3))

# Problem A3
# def find_trending_materials(brands):
#         res = []
#         unique = set()
#         for x in brands:
#             for y in x.get("materials"):
#                 if y not in unique:
#                     unique.add(y)
#                 else:
#                     res.append(y)

#         return res


# brands = [
#     {"name": "EcoWear", "materials": ["organic cotton", "recycled polyester"]},
#     {"name": "GreenThreads", "materials": ["organic cotton", "bamboo"]},
#     {"name": "SustainableStyle", "materials": ["bamboo", "recycled polyester"]}
# ]

# brands_2 = [
#     {"name": "NatureWear", "materials": ["hemp", "linen"]},
#     {"name": "Earthly", "materials": ["organic cotton", "hemp"]},
#     {"name": "GreenFit", "materials": ["linen", "recycled wool"]}
# ]

# brands_3 = [
#     {"name": "OrganicThreads", "materials": ["organic cotton"]},
#     {"name": "EcoFashion", "materials": ["recycled polyester", "hemp"]},
#     {"name": "GreenLife", "materials": ["recycled polyester", "bamboo"]}
# ]

# print(find_trending_materials(brands))
# print(find_trending_materials(brands_2))
# print(find_trending_materials(brands_3))

# Problem A4

def find_best_fabric_pair(fabrics, budget):
    sorted_fabrics = sorted(fabrics, key=lambda x: x[1])
    left = 0
    right = len(sorted_fabrics) - 1
    global_max = float("-inf")
    res = tuple()
    

    while left < right:
        cur_sum = sorted_fabrics[left][1] + sorted_fabrics[right][1]
        if cur_sum <= budget:
            if cur_sum > global_max:
                global_max = cur_sum
                res = (sorted_fabrics[left][0], sorted_fabrics[right][0])
            left += 1
        else:
            right -= 1
    return res


fabrics = [("Organic Cotton", 30), ("Recycled Polyester", 20), ("Bamboo", 25), ("Hemp", 15)]
fabrics_2 = [("Linen", 50), ("Recycled Wool", 40), ("Tencel", 30), ("Organic Cotton", 60)]
fabrics_3 = [("Linen", 40), ("Hemp", 35), ("Recycled Polyester", 25), ("Bamboo", 20)]

print(find_best_fabric_pair(fabrics, 45))
print(find_best_fabric_pair(fabrics_2, 70))
print(find_best_fabric_pair(fabrics_3, 60))