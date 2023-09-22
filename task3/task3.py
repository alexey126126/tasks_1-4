import json


class Segment:
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end

    def length_segment(self):
        return self.end - self.begin


def write_json_file(file_name, data):
    with open(file_name, "w") as json_file:
        json.dump([s.__dict__ for s in data], json_file, indent=2)


def read_json_file(file_name):
    with open(file_name, "r") as file:
        segment_data = json.load(file)
    # Преобразование данных в экземпляры класса
    return [Segment(data["begin"], data["end"]) for data in segment_data]


arr_segment = read_json_file("input.json")


def segment_union(segments):
    max_length = 0
    tmp_len = 0
    max_sum_segment = []
    segments = sorted(segments, key=lambda segment: segment.begin)
    for i in range(len(segments) - 2):
        for j in range(i + 1, len(segments) - 1):
            for k in range(j + 1, len(segments)):
                if (segments[i].end < segments[j].begin) and (segments[j].end < segments[k].begin):
                    tmp_len = segments[i].length_segment + segments[j].length_segment + segments[k].length_segment
                    if tmp_len > max_length:
                        max_length = tmp_len
                        max_sum_segment.clear()
                        max_sum_segment.append(segments[i])
                        max_sum_segment.append(segments[j])
                        max_sum_segment.append(segments[k])
    return max_sum_segment


write_json_file("output1.json", segment_union(arr_segment))


print('\n'.join(
    [str(i.__dict__) for i in segment_union(arr_segment)]))
