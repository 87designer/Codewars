def data_reverse(data):
    segmented_data = []
    for i in range(0,len(data),8):
        segmented_data.append(data[i:i+8])
    segmented_data.reverse()
    reversed_data = []
    for segment in segmented_data:
        reversed_data.extend(segment)
    return reversed_data
