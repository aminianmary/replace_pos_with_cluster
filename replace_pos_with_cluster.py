import codecs, sys, math
from collections import defaultdict

clusters_reader = codecs.open(sys.argv[1], 'r')
input_reader = codecs.open(sys.argv[2], 'r') #conll09 format
output_fp = sys.argv[3]
clusters = defaultdict(int)
four_bit_clusters = defaultdict(int)
unk_cluster= "UNK"

def get_four_bit_cluster(full_cluster):
    full_cluster_bits = list(full_cluster)
    four_bit_clusters = full_cluster_bits[0: min(4, len(full_cluster_bits))]
    return ''.join(four_bit_clusters)

for line in clusters_reader:
    split  = line.split('\t')
    w = split[1]
    cluster = split[0]
    four_bit_cluster = get_four_bit_cluster(cluster)
    clusters[w] = cluster
    four_bit_clusters[w] = four_bit_cluster

with codecs.open(output_fp, 'w') as writer, codecs.open(output_fp+'.short_cluster', 'w') as short_cluster_writer:
    for line in input_reader:
        if line != '\n':
            split = line.split('\t')
            word = split[1]
            c = clusters[word] if word in clusters else unk_cluster
            sc = four_bit_clusters[word] if word in four_bit_clusters else unk_cluster
            writer.write('\t'.join(split[0:5])+'\t'+c+'\t'+'\t'.join(split[6:]))
            short_cluster_writer.write('\t'.join(split[0:5])+'\t'+sc+'\t'+'\t'.join(split[6:]))

        else:
            writer.write('\n')
            short_cluster_writer.write('\n')
    writer.flush()
    writer.close()



