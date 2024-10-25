pairs = list(map(str.splitlines, open('sample.txt').read().split('\n\n')))

for pair in pairs:
    top, bottom = pair
    top_lists = top.split(']')
    top_items = [item.split(',') for item in top_lists]

# for pair in pairs:
#     raw_top_list, raw_bottom_list = pair.split('\n')
#     print(raw_top_list)
#     print(raw_bottom_list)
#     print(eval('sum(raw_bottom_list)'))
#     lists_top = raw_top_list.split(']')
#     lists_bottom = raw_bottom_list.split(']')
#
#     print(lists_top)
#     print(lists_bottom)
#     print(raw_top_list)
#     print(raw_bottom_list)
#     print('_' * 125)
#     # top_list = raw_top_list[1:-1].split(',')
#     # bottom_list = raw_bottom_list[1:-1].split(',')
#
#     for location_top, location_bottom in zip(lists_top, lists_bottom):
#         if location_top == '' and location_bottom == '':
#             continue
#         if location_top[0] == ',':
#             location_top = location_top[0:]
#         if location_bottom[0] == ',':
#             location_bottom = location_bottom[0:]
#         elif not location_top.startswith('[') and not location_bottom.startswith('['):
#             print(location_top)
#             print(location_bottom)
#             quit()
#         elif location_top.startswith('[') and not location_bottom.startswith('['):
#             print('1 list right')
#         elif not location_top.startswith('[') and location_bottom.startswith('['):
#             print('1 int left')
#         else:
#             print('2 lists')