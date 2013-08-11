<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
   "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml"
      xmlns:meld="http://www.plope.com/software/meld3">
<head>
  <title>Supervisor Status</title>
  <link href="static/dashboard.css" rel="stylesheet" type="text/css" />
  <link href="static/icon.png" rel="icon" type="image/png" />
</head>
<body>
<div id="wrapper">

  <div id="header">
    <h1>Supervisor Aggregator</h1>
  </div>

% for s in summaries:
      <h1><a href="http://{{s['hostname']}}:{{s['port']}}">{{s['hostname']}}</a>: <div class="state-{{s['serverStatus'].lower()}}">{{s['serverStatus']}}</div></h1>
      <table cellspacing="0" meld:id="statustable">
        <thead>
        <tr>
          <th class="state">State</th>
          <th class="desc">Description</th>
          <th class="name">Name</th>
        </tr>
        </thead>

        <tbody meld:id="tbody"
%         for ps in s['statuses']:
          <tr meld:id="tr" class="">
            <td class="status"><div class="state-{{ps['statename'].lower()}}">{{ps['statename']}}</div></td>
            <td>{{ps['description']}}</td>
            <td>{{ps['name']}}</td>
          </tr>
%         end
        </tbody>
      </table>
% end

</div>
<div class="push"></div>
</body>
</html>
