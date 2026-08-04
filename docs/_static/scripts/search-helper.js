var SEARCH_TRIGGER_DELAY_MS = 500;

function findnow(term) {
    var s = document.querySelector('input.md-search__input');
    if (!s) {
        return;
    }

    // Returned to simple search term, so open the search box and populate it with the term.
    setTimeout(function() {
        s.focus();
        s.value=term;
        s.dispatchEvent(new Event('input', { bubbles: true }));
    }, SEARCH_TRIGGER_DELAY_MS);
}


function getSearchTermFromHref(href) {
    if (!href) {
        return null;
    }

    if (href.startsWith('#')) {
        return null;
    }

    if (/^(mailto:|tel:|javascript:)/i.test(href)) {
        return null;
    }

    var url;
    try {
        url = new URL(href, window.location.href);
    } catch (e) {
        return null;
    }

    // Only intercept links that stay on this site.
    if (url.origin !== window.location.origin) {
        return null;
    }

    // Only accept links in the form /?term (no key=value pairs).
    var rawQuery = url.search ? url.search.substring(1) : '';
    if (!rawQuery || rawQuery.includes('=')) {
        return null;
    }

    return decodeURIComponent(rawQuery);
}

// Delegated click handling means dynamically added links work automatically.
if (!document.__searchHelperDelegatedBound) {
    document.addEventListener('click', function(event) {
        var link = event.target.closest('a[href]');
        if (!link) {
            return;
        }

        var searchTerm = getSearchTermFromHref(link.getAttribute('href'));
        if (!searchTerm) {
            return;
        }

        event.preventDefault();
        event.stopPropagation();
        event.stopImmediatePropagation();

        findnow(searchTerm);
    });

    document.__searchHelperDelegatedBound = true;
}
