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


def segment_union(segments):
    max_length = 0
    res_segments = []
    segments = sorted(segments, key=lambda segment: segment.begin)

    for i in range(len(segments) - 2):
        for j in range(i + 1, len(segments) - 1):
            if segments[i].end >= segments[j].begin:
                continue
            for k in range(j + 1, len(segments)):
                if segments[j].end >= segments[k].begin:
                    continue
                tmp_len = segments[i].length_segment() + segments[j].length_segment() + segments[k].length_segment()
                if max_length < tmp_len:
                    max_length = tmp_len
                    res_segments = [segments[i], segments[j], segments[k]]
    return res_segments, max_length


segments = read_json_file("input.json")

print('\n'.join([str(i.__dict__) for i in sorted(segments, key=lambda segment: segment.begin)]))

res, max_len = segment_union(segments)

print('res:')
print('max_len:', max_len)

print('\n'.join([str(i.__dict__) for i in res]))
