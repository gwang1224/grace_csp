---
keywords: fastai
description: Observing hashmaps with python dictionaries
title: Data Structures- Hashmaps, Sets, Hash Tables, Hashing and Collisions
toc: true
categories: [trimester 3]
nb_path: _notebooks/2023-03-29-DS-hashmaps.ipynb
layout: notebook
---

<!--
#################################################
### THIS FILE WAS AUTOGENERATED! DO NOT EDIT! ###
#################################################
# file to edit: _notebooks/2023-03-29-DS-hashmaps.ipynb
-->

<div class="container" id="notebook-container">
        
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="What-is-a-Hashtable/Hashmap?">What is a Hashtable/Hashmap?<a class="anchor-link" href="#What-is-a-Hashtable/Hashmap?"> </a></h2><blockquote><p>A hashtable is a data structure that with a collection of key-value pairs, where each key maps to a value, and the keys must be unique and hashable.</p>
</blockquote>
<ul>
<li>In Python there is a built in hashtable known as a dictionary.</li>
</ul>
<blockquote><p>The primary purpose of a hashtable is to provide efficient lookup, insertion, and deletion operations. When an element is to be inserted into the hashtable, a hash function is used to map the key to a specific index in the underlying array that is used to store the key-value pairs. The value is then stored at that index. When searching for a value, the hash function is used again to find the index where the value is stored.</p>
<p>The key advantage of a hashtable over other data structures like arrays and linked lists is its average-case time complexity for lookup, insertion, and deletion operations.</p>
</blockquote>
<ul>
<li>The typical time complexity of a hashtable is O(1). </li>
</ul>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="What-is-Hashing-and-Collision?">What is Hashing and Collision?<a class="anchor-link" href="#What-is-Hashing-and-Collision?"> </a></h2><blockquote><p>Hashing is the process of mapping a given key to a value in a hash table or hashmap, using a hash function. The hash function takes the key as input and produces a hash value or hash code, which is then used to determine the index in the underlying array where the value is stored. The purpose of hashing is to provide a quick and efficient way to access data, by eliminating the need to search through an entire data structure to find a value.</p>
<p>However, it is possible for two different keys to map to the same hash value, resulting in a collision. When a collision occurs, there are different ways to resolve it, depending on the collision resolution strategy used.</p>
<p>Python's dictionary implementation is optimized to handle collisions efficiently, and the performance of the dictionary is generally very good, even in the presence of collisions. However, if the number of collisions is very high, the performance of the dictionary can degrade, so it is important to choose a good hash function that minimizes collisions when designing a Python dictionary.</p>
</blockquote>
<h2 id="What-is-a-Set?">What is a Set?<a class="anchor-link" href="#What-is-a-Set?"> </a></h2>
</div>
</div>
</div>
    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">my_set</span> <span class="o">=</span> <span class="nb">set</span><span class="p">([</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">1</span><span class="p">])</span>
<span class="nb">print</span><span class="p">(</span><span class="n">my_set</span><span class="p">)</span>  

<span class="c1"># What do you notice in the output?</span>
<span class="c1"># </span>
<span class="c1"># The output prints out 3 numbers and doesn&#39;t repeat the values in the set. </span>

<span class="c1"># Why do you think Sets are in the same tech talk as Hashmaps/Hashtables?</span>
<span class="c1">#</span>
<span class="c1"># Sets are useful in removing duplicates from a list. </span>
<span class="c1"># Hash functions help preprocess data, which the set function can help do.</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">

<div class="output_subarea output_stream output_stdout output_text">
<pre>{1, 2, 3}
</pre>
</div>
</div>

</div>
</div>

</div>
    {% endraw %}

<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Dictionary-Example">Dictionary Example<a class="anchor-link" href="#Dictionary-Example"> </a></h2><p>Below are just some basic features of a dictionary. As always, documentation is always the main source for all the full capablilties.</p>

</div>
</div>
</div>
    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">lover_album</span> <span class="o">=</span> <span class="p">{</span>
    <span class="s2">&quot;title&quot;</span><span class="p">:</span> <span class="s2">&quot;Lover&quot;</span><span class="p">,</span>
    <span class="s2">&quot;artist&quot;</span><span class="p">:</span> <span class="s2">&quot;Taylor Swift&quot;</span><span class="p">,</span>
    <span class="s2">&quot;year&quot;</span><span class="p">:</span> <span class="mi">2019</span><span class="p">,</span>
    <span class="s2">&quot;genre&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;Pop&quot;</span><span class="p">,</span> <span class="s2">&quot;Synth-pop&quot;</span><span class="p">],</span>
    <span class="s2">&quot;tracks&quot;</span><span class="p">:</span> <span class="p">{</span>
        <span class="mi">1</span><span class="p">:</span> <span class="s2">&quot;I Forgot That You Existed&quot;</span><span class="p">,</span>
        <span class="mi">2</span><span class="p">:</span> <span class="s2">&quot;Cruel Summer&quot;</span><span class="p">,</span>
        <span class="mi">3</span><span class="p">:</span> <span class="s2">&quot;Lover&quot;</span><span class="p">,</span>
        <span class="mi">4</span><span class="p">:</span> <span class="s2">&quot;The Man&quot;</span><span class="p">,</span>
        <span class="mi">5</span><span class="p">:</span> <span class="s2">&quot;The Archer&quot;</span><span class="p">,</span>
        <span class="mi">6</span><span class="p">:</span> <span class="s2">&quot;I Think He Knows&quot;</span><span class="p">,</span>
        <span class="mi">7</span><span class="p">:</span> <span class="s2">&quot;Miss Americana &amp; The Heartbreak Prince&quot;</span><span class="p">,</span>
        <span class="mi">8</span><span class="p">:</span> <span class="s2">&quot;Paper Rings&quot;</span><span class="p">,</span>
        <span class="mi">9</span><span class="p">:</span> <span class="s2">&quot;Cornelia Street&quot;</span><span class="p">,</span>
        <span class="mi">10</span><span class="p">:</span> <span class="s2">&quot;Death By A Thousand Cuts&quot;</span><span class="p">,</span>
        <span class="mi">11</span><span class="p">:</span> <span class="s2">&quot;London Boy&quot;</span><span class="p">,</span>
        <span class="mi">12</span><span class="p">:</span> <span class="s2">&quot;Soon You&#39;ll Get Better (feat. Dixie Chicks)&quot;</span><span class="p">,</span>
        <span class="mi">13</span><span class="p">:</span> <span class="s2">&quot;False God&quot;</span><span class="p">,</span>
        <span class="mi">14</span><span class="p">:</span> <span class="s2">&quot;You Need To Calm Down&quot;</span><span class="p">,</span>
        <span class="mi">15</span><span class="p">:</span> <span class="s2">&quot;Afterglow&quot;</span><span class="p">,</span>
        <span class="mi">16</span><span class="p">:</span> <span class="s2">&quot;Me! (feat. Brendon Urie of Panic! At The Disco)&quot;</span><span class="p">,</span>
        <span class="mi">17</span><span class="p">:</span> <span class="s2">&quot;It&#39;s Nice To Have A Friend&quot;</span><span class="p">,</span>
        <span class="mi">18</span><span class="p">:</span> <span class="s2">&quot;Daylight&quot;</span>
    <span class="p">}</span>
<span class="p">}</span>

<span class="c1"># What data structures do you see?</span>
<span class="c1"># Data structures used are dictionary, list, and set.</span>

<span class="c1"># Printing the dictionary</span>
<span class="nb">print</span><span class="p">(</span><span class="n">lover_album</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">

<div class="output_subarea output_stream output_stdout output_text">
<pre>{&#39;title&#39;: &#39;Lover&#39;, &#39;artist&#39;: &#39;Taylor Swift&#39;, &#39;year&#39;: 2019, &#39;genre&#39;: [&#39;Pop&#39;, &#39;Synth-pop&#39;], &#39;tracks&#39;: {1: &#39;I Forgot That You Existed&#39;, 2: &#39;Cruel Summer&#39;, 3: &#39;Lover&#39;, 4: &#39;The Man&#39;, 5: &#39;The Archer&#39;, 6: &#39;I Think He Knows&#39;, 7: &#39;Miss Americana &amp; The Heartbreak Prince&#39;, 8: &#39;Paper Rings&#39;, 9: &#39;Cornelia Street&#39;, 10: &#39;Death By A Thousand Cuts&#39;, 11: &#39;London Boy&#39;, 12: &#34;Soon You&#39;ll Get Better (feat. Dixie Chicks)&#34;, 13: &#39;False God&#39;, 14: &#39;You Need To Calm Down&#39;, 15: &#39;Afterglow&#39;, 16: &#39;Me! (feat. Brendon Urie of Panic! At The Disco)&#39;, 17: &#34;It&#39;s Nice To Have A Friend&#34;, 18: &#39;Daylight&#39;}}
</pre>
</div>
</div>

</div>
</div>

</div>
    {% endraw %}

    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="n">lover_album</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">&#39;tracks&#39;</span><span class="p">))</span>
<span class="c1"># or</span>
<span class="nb">print</span><span class="p">(</span><span class="n">lover_album</span><span class="p">[</span><span class="s1">&#39;tracks&#39;</span><span class="p">])</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">

<div class="output_subarea output_stream output_stdout output_text">
<pre>{1: &#39;I Forgot That You Existed&#39;, 2: &#39;Cruel Summer&#39;, 3: &#39;Lover&#39;, 4: &#39;The Man&#39;, 5: &#39;The Archer&#39;, 6: &#39;I Think He Knows&#39;, 7: &#39;Miss Americana &amp; The Heartbreak Prince&#39;, 8: &#39;Paper Rings&#39;, 9: &#39;Cornelia Street&#39;, 10: &#39;Death By A Thousand Cuts&#39;, 11: &#39;London Boy&#39;, 12: &#34;Soon You&#39;ll Get Better (feat. Dixie Chicks)&#34;, 13: &#39;False God&#39;, 14: &#39;You Need To Calm Down&#39;, 15: &#39;Afterglow&#39;, 16: &#39;Me! (feat. Brendon Urie of Panic! At The Disco)&#39;, 17: &#34;It&#39;s Nice To Have A Friend&#34;, 18: &#39;Daylight&#39;}
{1: &#39;I Forgot That You Existed&#39;, 2: &#39;Cruel Summer&#39;, 3: &#39;Lover&#39;, 4: &#39;The Man&#39;, 5: &#39;The Archer&#39;, 6: &#39;I Think He Knows&#39;, 7: &#39;Miss Americana &amp; The Heartbreak Prince&#39;, 8: &#39;Paper Rings&#39;, 9: &#39;Cornelia Street&#39;, 10: &#39;Death By A Thousand Cuts&#39;, 11: &#39;London Boy&#39;, 12: &#34;Soon You&#39;ll Get Better (feat. Dixie Chicks)&#34;, 13: &#39;False God&#39;, 14: &#39;You Need To Calm Down&#39;, 15: &#39;Afterglow&#39;, 16: &#39;Me! (feat. Brendon Urie of Panic! At The Disco)&#39;, 17: &#34;It&#39;s Nice To Have A Friend&#34;, 18: &#39;Daylight&#39;}
</pre>
</div>
</div>

</div>
</div>

</div>
    {% endraw %}

    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="n">lover_album</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">&#39;tracks&#39;</span><span class="p">)[</span><span class="mi">4</span><span class="p">])</span>
<span class="c1"># or</span>
<span class="nb">print</span><span class="p">(</span><span class="n">lover_album</span><span class="p">[</span><span class="s1">&#39;tracks&#39;</span><span class="p">][</span><span class="mi">4</span><span class="p">])</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">

<div class="output_subarea output_stream output_stdout output_text">
<pre>The Man
The Man
</pre>
</div>
</div>

</div>
</div>

</div>
    {% endraw %}

    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># What can you change to make sure there are no duplicate producers?</span>

<span class="n">lover_album</span><span class="p">[</span><span class="s2">&quot;producer&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="nb">set</span><span class="p">([</span><span class="s1">&#39;Taylor Swift&#39;</span><span class="p">,</span> <span class="s1">&#39;Jack Antonoff&#39;</span><span class="p">,</span> <span class="s1">&#39;Joel Little&#39;</span><span class="p">,</span> <span class="s1">&#39;Taylor Swift&#39;</span><span class="p">,</span> <span class="s1">&#39;Louis Bell&#39;</span><span class="p">,</span> <span class="s1">&#39;Frank Dukes&#39;</span><span class="p">]))</span>

<span class="c1"># Printing the dictionary</span>
<span class="nb">print</span><span class="p">(</span><span class="n">lover_album</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">

<div class="output_subarea output_stream output_stdout output_text">
<pre>{&#39;title&#39;: &#39;Lover&#39;, &#39;artist&#39;: &#39;Taylor Swift&#39;, &#39;year&#39;: 2019, &#39;genre&#39;: [&#39;Pop&#39;, &#39;Synth-pop&#39;], &#39;tracks&#39;: {1: &#39;I Forgot That You Existed&#39;, 2: &#39;Cruel Summer&#39;, 3: &#39;Lover&#39;, 4: &#39;The Man&#39;, 5: &#39;The Archer&#39;, 6: &#39;I Think He Knows&#39;, 7: &#39;Miss Americana &amp; The Heartbreak Prince&#39;, 8: &#39;Paper Rings&#39;, 9: &#39;Cornelia Street&#39;, 10: &#39;Death By A Thousand Cuts&#39;, 11: &#39;London Boy&#39;, 12: &#34;Soon You&#39;ll Get Better (feat. Dixie Chicks)&#34;, 13: &#39;False God&#39;, 14: &#39;You Need To Calm Down&#39;, 15: &#39;Afterglow&#39;, 16: &#39;Me! (feat. Brendon Urie of Panic! At The Disco)&#39;, 17: &#34;It&#39;s Nice To Have A Friend&#34;, 18: &#39;Daylight&#39;}, &#39;producer&#39;: [&#39;Frank Dukes&#39;, &#39;Joel Little&#39;, &#39;Taylor Swift&#39;, &#39;Louis Bell&#39;, &#39;Jack Antonoff&#39;]}
</pre>
</div>
</div>

</div>
</div>

</div>
    {% endraw %}

    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">lover_album</span><span class="p">[</span><span class="s2">&quot;tracks&quot;</span><span class="p">]</span><span class="o">.</span><span class="n">update</span><span class="p">({</span><span class="mi">19</span><span class="p">:</span> <span class="s2">&quot;All Of The Girls You Loved Before&quot;</span><span class="p">})</span>

<span class="c1"># How would add an additional genre to the dictionary, like electropop? </span>

<span class="n">lover_album</span><span class="p">[</span><span class="s2">&quot;genre&quot;</span><span class="p">]</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s2">&quot;electropop&quot;</span><span class="p">)</span>

<span class="c1"># Printing the dictionary</span>
<span class="nb">print</span><span class="p">(</span><span class="n">lover_album</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">

<div class="output_subarea output_stream output_stdout output_text">
<pre>{&#39;title&#39;: &#39;Lover&#39;, &#39;artist&#39;: &#39;Taylor Swift&#39;, &#39;year&#39;: 2019, &#39;genre&#39;: [&#39;Pop&#39;, &#39;Synth-pop&#39;, &#39;electropop&#39;], &#39;tracks&#39;: {1: &#39;I Forgot That You Existed&#39;, 2: &#39;Cruel Summer&#39;, 3: &#39;Lover&#39;, 4: &#39;The Man&#39;, 5: &#39;The Archer&#39;, 6: &#39;I Think He Knows&#39;, 7: &#39;Miss Americana &amp; The Heartbreak Prince&#39;, 8: &#39;Paper Rings&#39;, 9: &#39;Cornelia Street&#39;, 10: &#39;Death By A Thousand Cuts&#39;, 11: &#39;London Boy&#39;, 12: &#34;Soon You&#39;ll Get Better (feat. Dixie Chicks)&#34;, 13: &#39;False God&#39;, 14: &#39;You Need To Calm Down&#39;, 15: &#39;Afterglow&#39;, 16: &#39;Me! (feat. Brendon Urie of Panic! At The Disco)&#39;, 17: &#34;It&#39;s Nice To Have A Friend&#34;, 18: &#39;Daylight&#39;, 19: &#39;All Of The Girls You Loved Before&#39;}, &#39;producer&#39;: [&#39;Frank Dukes&#39;, &#39;Joel Little&#39;, &#39;Taylor Swift&#39;, &#39;Louis Bell&#39;, &#39;Jack Antonoff&#39;]}
</pre>
</div>
</div>

</div>
</div>

</div>
    {% endraw %}

    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">for</span> <span class="n">k</span><span class="p">,</span><span class="n">v</span> <span class="ow">in</span> <span class="n">lover_album</span><span class="o">.</span><span class="n">items</span><span class="p">():</span> <span class="c1"># iterate using a for loop for key and value</span>
    <span class="nb">print</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">k</span><span class="p">)</span> <span class="o">+</span> <span class="s2">&quot;: &quot;</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">v</span><span class="p">))</span>

<span class="c1"># Write your own code to print tracks in readable format</span>
<span class="n">tracks_dict</span> <span class="o">=</span> <span class="n">lover_album</span><span class="p">[</span><span class="s2">&quot;tracks&quot;</span><span class="p">]</span>
<span class="n">track</span> <span class="o">=</span> <span class="mi">1</span>
<span class="k">for</span> <span class="n">song</span> <span class="ow">in</span> <span class="n">tracks_dict</span><span class="o">.</span><span class="n">values</span><span class="p">():</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Track &quot;</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">track</span><span class="p">)</span> <span class="o">+</span> <span class="s2">&quot;: &quot;</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">song</span><span class="p">))</span>
    <span class="n">track</span> <span class="o">+=</span> <span class="mi">1</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">

<div class="output_subarea output_stream output_stdout output_text">
<pre>title: Lover
artist: Taylor Swift
year: 2019
genre: [&#39;Pop&#39;, &#39;Synth-pop&#39;, &#39;electropop&#39;]
tracks: {1: &#39;I Forgot That You Existed&#39;, 2: &#39;Cruel Summer&#39;, 3: &#39;Lover&#39;, 4: &#39;The Man&#39;, 5: &#39;The Archer&#39;, 6: &#39;I Think He Knows&#39;, 7: &#39;Miss Americana &amp; The Heartbreak Prince&#39;, 8: &#39;Paper Rings&#39;, 9: &#39;Cornelia Street&#39;, 10: &#39;Death By A Thousand Cuts&#39;, 11: &#39;London Boy&#39;, 12: &#34;Soon You&#39;ll Get Better (feat. Dixie Chicks)&#34;, 13: &#39;False God&#39;, 14: &#39;You Need To Calm Down&#39;, 15: &#39;Afterglow&#39;, 16: &#39;Me! (feat. Brendon Urie of Panic! At The Disco)&#39;, 17: &#34;It&#39;s Nice To Have A Friend&#34;, 18: &#39;Daylight&#39;, 19: &#39;All Of The Girls You Loved Before&#39;}
producer: [&#39;Frank Dukes&#39;, &#39;Joel Little&#39;, &#39;Taylor Swift&#39;, &#39;Louis Bell&#39;, &#39;Jack Antonoff&#39;]
Track 1: I Forgot That You Existed
Track 2: Cruel Summer
Track 3: Lover
Track 4: The Man
Track 5: The Archer
Track 6: I Think He Knows
Track 7: Miss Americana &amp; The Heartbreak Prince
Track 8: Paper Rings
Track 9: Cornelia Street
Track 10: Death By A Thousand Cuts
Track 11: London Boy
Track 12: Soon You&#39;ll Get Better (feat. Dixie Chicks)
Track 13: False God
Track 14: You Need To Calm Down
Track 15: Afterglow
Track 16: Me! (feat. Brendon Urie of Panic! At The Disco)
Track 17: It&#39;s Nice To Have A Friend
Track 18: Daylight
Track 19: All Of The Girls You Loved Before
</pre>
</div>
</div>

</div>
</div>

</div>
    {% endraw %}

    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">search</span><span class="p">():</span>
    <span class="n">search</span> <span class="o">=</span> <span class="nb">input</span><span class="p">(</span><span class="s2">&quot;What would you like to know about the album?&quot;</span><span class="p">)</span>
    <span class="k">if</span> <span class="n">lover_album</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">search</span><span class="o">.</span><span class="n">lower</span><span class="p">())</span> <span class="o">==</span> <span class="kc">None</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Invalid Search&quot;</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="n">lover_album</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">search</span><span class="o">.</span><span class="n">lower</span><span class="p">()))</span>

<span class="n">search</span><span class="p">()</span>

<span class="c1"># This is a very basic code segment, how can you improve upon this code?</span>
<span class="c1"># We can add a feature that includes crud methods. This could be that when the topic is searched,</span>
<span class="c1"># something can be updated or deleted using the search definition as well. We can also add more text</span>
<span class="c1"># so that when the artist is asked it prints out a full sentence.</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">

<div class="output_subarea output_stream output_stdout output_text">
<pre>Taylor Swift
</pre>
</div>
</div>

</div>
</div>

</div>
    {% endraw %}

<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Hacks">Hacks<a class="anchor-link" href="#Hacks"> </a></h2><ul>
<li>What are the pro and cons of using this data structure? </li>
<li>Dictionary vs List   </li>
</ul>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p><img src="images/list.png" alt="Lists"></p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p><img src="/repository_1/images/copied_from_nb/images/dictionaries.png" alt="Dictionaries"></p>

</div>
</div>
</div>
    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">midnights_album</span> <span class="o">=</span> <span class="p">{</span>
    <span class="s2">&quot;title&quot;</span><span class="p">:</span> <span class="s2">&quot;Midnight 3 am&quot;</span><span class="p">,</span>
    <span class="s2">&quot;artist&quot;</span><span class="p">:</span> <span class="s2">&quot;Taylor Swift&quot;</span><span class="p">,</span>
    <span class="s2">&quot;year&quot;</span><span class="p">:</span> <span class="mi">2022</span><span class="p">,</span>
    <span class="s2">&quot;genre&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;Pop&quot;</span><span class="p">,</span> <span class="s2">&quot;Synth-pop&quot;</span><span class="p">,</span> <span class="s2">&quot;Alternative/Indie&quot;</span><span class="p">],</span>
    <span class="s2">&quot;tracks&quot;</span><span class="p">:</span> <span class="p">{</span>
        <span class="mi">1</span><span class="p">:</span> <span class="s2">&quot;Lavender Haze&quot;</span><span class="p">,</span>
        <span class="mi">2</span><span class="p">:</span> <span class="s2">&quot;Maroon&quot;</span><span class="p">,</span>
        <span class="mi">3</span><span class="p">:</span> <span class="s2">&quot;Anti-Hero&quot;</span><span class="p">,</span>
        <span class="mi">4</span><span class="p">:</span> <span class="s2">&quot;Snow on the Beach&quot;</span><span class="p">,</span>
        <span class="mi">5</span><span class="p">:</span> <span class="s2">&quot;You&#39;re on Your Own Kids&quot;</span><span class="p">,</span>
        <span class="mi">6</span><span class="p">:</span> <span class="s2">&quot;Midnight Rain&quot;</span><span class="p">,</span>
        <span class="mi">7</span><span class="p">:</span> <span class="s2">&quot;Question...?&quot;</span><span class="p">,</span>
        <span class="mi">8</span><span class="p">:</span> <span class="s2">&quot;Vigilante Sh*t&quot;</span><span class="p">,</span>
        <span class="mi">9</span><span class="p">:</span> <span class="s2">&quot;Bejeweled&quot;</span><span class="p">,</span>
        <span class="mi">10</span><span class="p">:</span> <span class="s2">&quot;Labyrinth&quot;</span><span class="p">,</span>
        <span class="mi">11</span><span class="p">:</span> <span class="s2">&quot;Karma&quot;</span><span class="p">,</span>
        <span class="mi">12</span><span class="p">:</span> <span class="s2">&quot;Sweet Nothing&quot;</span><span class="p">,</span>
        <span class="mi">13</span><span class="p">:</span> <span class="s2">&quot;Mastermind&quot;</span><span class="p">,</span>
        <span class="mi">14</span><span class="p">:</span> <span class="s2">&quot;The Great War&quot;</span><span class="p">,</span>
        <span class="mi">15</span><span class="p">:</span> <span class="s2">&quot;Bigger Than The Whole Sky&quot;</span><span class="p">,</span>
        <span class="mi">16</span><span class="p">:</span> <span class="s2">&quot;Paris&quot;</span><span class="p">,</span>
        <span class="mi">17</span><span class="p">:</span> <span class="s2">&quot;High Infidelity&quot;</span><span class="p">,</span>
        <span class="mi">18</span><span class="p">:</span> <span class="s2">&quot;Glitch&quot;</span><span class="p">,</span>
        <span class="mi">19</span><span class="p">:</span> <span class="s2">&quot;Would&#39;ve, Could&#39;ve, Should&#39;ve&quot;</span><span class="p">,</span>
        <span class="mi">20</span><span class="p">:</span> <span class="s2">&quot;Dear Reader&quot;</span>
    <span class="p">}</span>
<span class="p">}</span>
</pre></div>

    </div>
</div>
</div>

</div>
    {% endraw %}

    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="n">midnights_album</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">&#39;tracks&#39;</span><span class="p">))</span>
<span class="c1"># or</span>
<span class="nb">print</span><span class="p">(</span><span class="n">midnights_album</span><span class="p">[</span><span class="s1">&#39;tracks&#39;</span><span class="p">])</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">

<div class="output_subarea output_stream output_stdout output_text">
<pre>{1: &#39;Lavender Haze&#39;, 2: &#39;Maroon&#39;, 3: &#39;Anti-Hero&#39;, 4: &#39;Snow on the Beach&#39;, 5: &#34;You&#39;re on Your Own Kids&#34;, 6: &#39;Midnight Rain&#39;, 7: &#39;Question...?&#39;, 8: &#39;Vigilante Sh*t&#39;, 9: &#39;Bejeweled&#39;, 10: &#39;Labyrinth&#39;, 11: &#39;Karma&#39;, 12: &#39;Sweet Nothing&#39;, 13: &#39;Mastermind&#39;, 14: &#39;The Great War&#39;, 15: &#39;Bigger Than The Whole Sky&#39;, 16: &#39;Paris&#39;, 17: &#39;High Infidelity&#39;, 18: &#39;Glitch&#39;, 19: &#34;Would&#39;ve, Could&#39;ve, Should&#39;ve&#34;, 20: &#39;Dear Reader&#39;}
{1: &#39;Lavender Haze&#39;, 2: &#39;Maroon&#39;, 3: &#39;Anti-Hero&#39;, 4: &#39;Snow on the Beach&#39;, 5: &#34;You&#39;re on Your Own Kids&#34;, 6: &#39;Midnight Rain&#39;, 7: &#39;Question...?&#39;, 8: &#39;Vigilante Sh*t&#39;, 9: &#39;Bejeweled&#39;, 10: &#39;Labyrinth&#39;, 11: &#39;Karma&#39;, 12: &#39;Sweet Nothing&#39;, 13: &#39;Mastermind&#39;, 14: &#39;The Great War&#39;, 15: &#39;Bigger Than The Whole Sky&#39;, 16: &#39;Paris&#39;, 17: &#39;High Infidelity&#39;, 18: &#39;Glitch&#39;, 19: &#34;Would&#39;ve, Could&#39;ve, Should&#39;ve&#34;, 20: &#39;Dear Reader&#39;}
</pre>
</div>
</div>

</div>
</div>

</div>
    {% endraw %}

    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">for</span> <span class="n">k</span><span class="p">,</span><span class="n">v</span> <span class="ow">in</span> <span class="n">midnights_album</span><span class="o">.</span><span class="n">items</span><span class="p">():</span> 
    <span class="nb">print</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">k</span><span class="p">)</span> <span class="o">+</span> <span class="s2">&quot;: &quot;</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">v</span><span class="p">))</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">

<div class="output_subarea output_stream output_stdout output_text">
<pre>title: Midnight 3 am
artist: Taylor Swift
year: 2022
genre: [&#39;Pop&#39;, &#39;Synth-pop&#39;, &#39;Alternative/Indie&#39;]
tracks: {1: &#39;Lavender Haze&#39;, 2: &#39;Maroon&#39;, 3: &#39;Anti-Hero&#39;, 4: &#39;Snow on the Beach&#39;, 5: &#34;You&#39;re on Your Own Kids&#34;, 6: &#39;Midnight Rain&#39;, 7: &#39;Question...?&#39;, 8: &#39;Vigilante Sh*t&#39;, 9: &#39;Bejeweled&#39;, 10: &#39;Labyrinth&#39;, 11: &#39;Karma&#39;, 12: &#39;Sweet Nothing&#39;, 13: &#39;Mastermind&#39;, 14: &#39;The Great War&#39;, 15: &#39;Bigger Than The Whole Sky&#39;, 16: &#39;Paris&#39;, 17: &#39;High Infidelity&#39;, 18: &#39;Glitch&#39;, 19: &#34;Would&#39;ve, Could&#39;ve, Should&#39;ve&#34;, 20: &#39;Dear Reader&#39;}
</pre>
</div>
</div>

</div>
</div>

</div>
    {% endraw %}

    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">tracks_dict</span> <span class="o">=</span> <span class="n">midnights_album</span><span class="p">[</span><span class="s2">&quot;tracks&quot;</span><span class="p">]</span>
<span class="n">track</span> <span class="o">=</span> <span class="mi">1</span>
<span class="k">for</span> <span class="n">song</span> <span class="ow">in</span> <span class="n">tracks_dict</span><span class="o">.</span><span class="n">values</span><span class="p">():</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Track &quot;</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">track</span><span class="p">)</span> <span class="o">+</span> <span class="s2">&quot;: &quot;</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">song</span><span class="p">))</span>
    <span class="n">track</span> <span class="o">+=</span> <span class="mi">1</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">

<div class="output_subarea output_stream output_stdout output_text">
<pre>Track 1: Lavender Haze
Track 2: Maroon
Track 3: Anti-Hero
Track 4: Snow on the Beach
Track 5: You&#39;re on Your Own Kids
Track 6: Midnight Rain
Track 7: Question...?
Track 8: Vigilante Sh*t
Track 9: Bejeweled
Track 10: Labyrinth
Track 11: Karma
Track 12: Sweet Nothing
Track 13: Mastermind
Track 14: The Great War
Track 15: Bigger Than The Whole Sky
Track 16: Paris
Track 17: High Infidelity
Track 18: Glitch
Track 19: Would&#39;ve, Could&#39;ve, Should&#39;ve
Track 20: Dear Reader
</pre>
</div>
</div>

</div>
</div>

</div>
    {% endraw %}

</div>
 

