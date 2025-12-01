<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Trivy Security Scan Report</title>
    <style>
        body { font-family: Arial, sans-serif; padding: 20px; }
        h1 { color: #4a148c; }
        .clean { color: green; font-weight: bold; }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        th, td {
            border: 1px solid #ccc;
            padding: 8px;
            text-align: left;
        }
        th { background-color: #efefef; }
    </style>
</head>
<body>

<h1>Trivy Security Scan Report</h1>

{{ if .Results }}
    {{ range .Results }}
        {{ if .Vulnerabilities }}
            <h2>Target: {{ .Target }}</h2>
            <table>
                <tr>
                    <th>ID</th>
                    <th>Severity</th>
                    <th>Package</th>
                    <th>Installed Version</th>
                    <th>Fixed Version</th>
                    <th>Description</th>
                </tr>
                {{ range .Vulnerabilities }}
                <tr>
                    <td>{{ .VulnerabilityID }}</td>
                    <td>{{ .Severity }}</td>
                    <td>{{ .PkgName }}</td>
                    <td>{{ .InstalledVersion }}</td>
                    <td>{{ .FixedVersion }}</td>
                    <td>{{ .Description }}</td>
                </tr>
                {{ end }}
            </table>
        {{ end }}
    {{ end }}
{{ else }}
    <p class="clean">✔ No HIGH or CRITICAL vulnerabilities found!</p>
{{ end }}

</body>
</html>