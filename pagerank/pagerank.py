import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    result={}
    N=len(corpus)

    base=(1-damping_factor)/N

    if len(corpus[page])!=0:
        Numlinks=len(corpus[page])
        base_changed=base+(damping_factor/Numlinks)
        for p in corpus.keys():
            if p in corpus[page]:
                result[p]=base_changed
            else:
                result[p]=base

    else:
        for p in corpus.keys():
            result[p]=1/N

    return result



def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    counter={page:0 for page in corpus}

    selected_page=random.choice(list(corpus.keys()))
    counter[selected_page]+=1


    for i in range(n-1):
        prob=transition_model(corpus,selected_page,damping_factor)
        selected_page=random.choices(
            population=list(prob.keys()),
            weights=list(prob.values()),
            k=1
        )[0]
        counter[selected_page]+=1

    Norm={page:0 for page in corpus}
    for page in counter:
        Norm[page]=counter[page]/n

    return Norm



def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    N=len(corpus.keys())
    ranks={page:1/N for page in corpus}

    while True:
        new_ranks={}
        for page in corpus:
            rank=(1-damping_factor)/N
            for p in corpus:
                if len(corpus[p])==0:
                    rank+=damping_factor*(ranks[p]/N)
                elif page in corpus[p]:
                    rank+=damping_factor*(ranks[p]/len(corpus[p]))

            new_ranks[page]=rank

        if all(abs(new_ranks[p]-ranks[p])<0.001 for p in ranks):
            return new_ranks
        ranks=new_ranks


if __name__ == "__main__":
    main()
