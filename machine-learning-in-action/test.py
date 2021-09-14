

instr_p = raw_input()
instr_q = raw_input()

entity_list = instr_p.strip().split(';')
struct_single = []
struct_entity = []
for i in range(len(entity_list)):
    line = entity_list[i]
    attr_list = line.split('|')
    loc = attr_list[0].find('_')
    attr_name = attr_list[0][0:loc]
    attr_list[0] = attr_list[0][loc + 1:len(attr_list[0])]
    struct_single.append(list(attr_name))
    struct_single.extend(attr_list)
    struct_entity.append(struct_single)

query_list = [instr_q[i] for i in range(len(instr_q))]
out_list = []
for i in range(len(struct_entity)):
    for j in range(len(struct_entity[i])):
        if instr_q.find(struct_entity[i][j]) != -1:
            out_list.append(struct_entity[i][0])
            out_list.append(struct_entity[i][j])
