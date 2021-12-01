function doHttpSig() {

    var navigator = {}; //fake a navigator object for the lib
    var window = {}; //fake a window object for the lib

    //import javascript jsrsasign
    eval(postman.getGlobalVariable("jsrsasign-js"));

    function computeHttpSignature(config, headerHash) {
      var template = 'keyId="${keyId}",algorithm="${algorithm}",headers="${headers}",signature="${signature}"',
          sig = template;

      // compute sig here
      var signingBase = '';
      config.headers.forEach(function(h){
        if (signingBase !== '') { signingBase += '\n'; }
        signingBase += h.toLowerCase() + ": " + headerHash[h];
      });

    var kjursig = new KJUR.crypto.Signature({"alg": "SHA256withRSA"});
    kjursig.init(config.secretkey);
    kjursig.updateString(signingBase);
    var hash = kjursig.sign();

      var signatureOptions = {
            keyId : config.keyId,
            algorithm: config.algorithm,
            headers: config.headers,
            signature : hextob64(hash)
          };

      // build sig string here
      Object.keys(signatureOptions).forEach(function(key) {
        var pattern = "${" + key + "}",
            value = (typeof signatureOptions[key] != 'string') ? signatureOptions[key].join(' ') : signatureOptions[key];
        sig = sig.replace(pattern, value);
      });

      return sig;
    }

    var curDate = new Date().toGMTString();
    var targetUrl = request.url.trim(); // there may be surrounding ws
    targetUrl = targetUrl.replace(new RegExp('^https?://[^/]+/'),'/'); // strip hostname
    var host = request.url.trim();
    host = host.replace(new RegExp('^https?://'), '');
    host = host.replace(new RegExp('/.*$'), '');
    var method = request.method.toLowerCase();
    var body = request.data;
    if (method == "get") {
        body="";
    }
    var sha256digest = CryptoJS.SHA256(body);
    var base64sha256 = CryptoJS.enc.Base64.stringify(sha256digest);
    var computedDigest = 'SHA-256=' + base64sha256;

    var headerHash = {
          date : curDate,
          digest : computedDigest,
          host : host,
          '(request-target)' : method + ' ' + targetUrl.toLowerCase()
        };

    var config = {
          algorithm : 'rsa-sha256',
          keyId : environment['key-id'],
          secretkey : environment['shared-secret'],
          headers : [ '(request-target)', 'date', 'digest', 'host' ]
        };
    var sig = computeHttpSignature(config, headerHash);

    postman.setEnvironmentVariable('httpsig', sig);
    postman.setEnvironmentVariable('computed-digest', computedDigest);
    postman.setEnvironmentVariable("current-date", curDate);
    postman.setEnvironmentVariable("target-url", targetUrl);
}


if (globals['jsrsasign-js'] === undefined ) {
    console.log("jsrasign library not already downloaded. Downloading now. ")

    pm.sendRequest({
        url: "http://kjur.github.io/jsrsasign/jsrsasign-latest-all-min.js",
        method: "GET",
        body: {}
    }, function (err, res) {
        postman.setGlobalVariable("jsrsasign-js", res.text());
    doHttpSig();
    });

} else {
    doHttpSig();
}
